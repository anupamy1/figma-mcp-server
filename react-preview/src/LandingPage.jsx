import React from 'react';
import './LandingPage.css';

import heroLocal from '../assets/hero.png';
import feature1Local from '../assets/feature1.png';
import feature2Local from '../assets/feature2.png';
import feature3Local from '../assets/feature3.png';

const FIGMA_MCP_BASE_URL = (typeof import.meta !== 'undefined' && import.meta.env && import.meta.env.VITE_FIGMA_MCP_URL) || 'http://localhost:5000';
const FIGMA_IMAGE_NODE_IDS = {
  hero: '1:1495',
  card1: '1:1499',
  card2: '1:1504',
  card3: '1:1509',
  side: '1:1513',
  bottom1: '1:1517',
  bottom2: '1:1522',
  avatar1: '1:1422',
  avatar2: '1:1429',
  avatar3: '1:1436'
};

const localFallbacks = {
  hero: heroLocal,
  card1: feature1Local,
  // feature2Local is a black placeholder asset — avoid using it for visible cards
  card2: feature3Local,
  card3: feature1Local,
  side: feature3Local,
  bottom1: feature3Local,
  bottom2: feature1Local,
  avatar1: feature1Local,
  avatar2: feature1Local,
  avatar3: feature3Local
};

const navLinks = ['Page', 'Page', 'Page'];

const getFigmaImage = (images, nodeId, fallback) => images[nodeId] || fallback;

function buildFeatureCards(images) {
  return [
    {
      title: 'Subheading',
      description: 'Body text for whatever you’d like to add more to the subheading.',
      image: getFigmaImage(images, FIGMA_IMAGE_NODE_IDS.card1, localFallbacks.card1),
      fallback: localFallbacks.card1
    },
    {
      title: 'Subheading',
      description: 'Body text for whatever you’d like to expand on the main point.',
      image: getFigmaImage(images, FIGMA_IMAGE_NODE_IDS.card2, localFallbacks.card2),
      fallback: localFallbacks.card2
    },
    {
      title: 'Subheading',
      description: 'Body text for whatever you’d like to share more.',
      image: getFigmaImage(images, FIGMA_IMAGE_NODE_IDS.card3, localFallbacks.card3),
      fallback: localFallbacks.card3
    }
  ];
}

const textBlocks = [
  { title: 'Subheading', description: 'Body text for whatever you’d like to expand on the main point.' },
  { title: 'Subheading', description: 'Body text for whatever you’d like to say. Add main takeaway points, quotes, anecdotes.' },
  { title: 'Subheading', description: 'Body text for whatever you’d like to add more to the main point. It provides details, explanations, and context.' }
];

function buildBottomCards(images) {
  return [
    {
      title: 'Subheading',
      description: 'Body text for whatever you’d like to add more to the subheading.',
      image: getFigmaImage(images, FIGMA_IMAGE_NODE_IDS.bottom1, localFallbacks.bottom1),
      fallback: localFallbacks.bottom1
    },
    {
      title: 'Subheading',
      description: 'Body text for whatever you’d like to expand on the main point.',
      image: getFigmaImage(images, FIGMA_IMAGE_NODE_IDS.bottom2, localFallbacks.bottom2),
      fallback: localFallbacks.bottom2
    }
  ];
}

function buildTestimonials(images) {
  return [
    {
      quote: '“A terrific piece of praise”',
      name: 'Ava Miles',
      description: 'Marketing lead at BrandCo',
      initials: 'AM',
      avatar: getFigmaImage(images, FIGMA_IMAGE_NODE_IDS.avatar1, localFallbacks.avatar1)
    },
    {
      quote: '“A fantastic bit of feedback”',
      name: 'Noah Patel',
      description: 'Founder at StartupX',
      initials: 'NP',
      avatar: getFigmaImage(images, FIGMA_IMAGE_NODE_IDS.avatar2, localFallbacks.avatar2)
    },
    {
      quote: '“A genuinely glowing review”',
      name: 'Mia Chen',
      description: 'Design director at Studio9',
      initials: 'MC',
      avatar: getFigmaImage(images, FIGMA_IMAGE_NODE_IDS.avatar3, localFallbacks.avatar3)
    }
  ];
}

const footerColumns = [
  { heading: 'Topic', items: ['Page', 'Page', 'Page'] },
  { heading: 'Topic', items: ['Page', 'Page', 'Page'] },
  { heading: 'Topic', items: ['Page', 'Page', 'Page'] }
];

function FeatureCard({ image, fallback, title, description }) {
  return (
    <article className="card">
      <img
        src={image || fallback}
        alt={title}
        onError={(e) => {
          if (fallback) e.currentTarget.src = fallback;
        }}
      />
      <div>
        <h3>{title}</h3>
        <p>{description}</p>
      </div>
    </article>
  );
}

function BottomCard({ image, fallback, title, description }) {
  return (
    <article className="card">
      <img
        src={image || fallback}
        alt={title}
        onError={(e) => {
          if (fallback) e.currentTarget.src = fallback;
        }}
      />
      <div>
        <h3>{title}</h3>
        <p>{description}</p>
      </div>
    </article>
  );
}

function Testimonial({ quote, name, description, initials, avatar }) {
  const [avatarError, setAvatarError] = React.useState(false);
  const showAvatar = avatar && !avatarError;

  return (
    <article className="testimonial">
      <blockquote className="testimonial-quote">{quote}</blockquote>
      <div className="avatar-row">
        <div className="avatar" aria-hidden="true">
          {showAvatar ? (
            <img
              src={avatar}
              alt={name}
              className="avatar-img"
              onError={() => setAvatarError(true)}
            />
          ) : (
            <div className="avatar-icon">{initials}</div>
          )}
        </div>
        <div>
          <div className="avatar-name">{name}</div>
          <div className="avatar-desc">{description}</div>
        </div>
      </div>
    </article>
  );
}

export default function LandingPage() {
  const [figmaImages, setFigmaImages] = React.useState({});

  React.useEffect(() => {
    async function fetchImageUrls() {
      try {
        const response = await fetch(`${FIGMA_MCP_BASE_URL}/figma-image-urls`);
        if (!response.ok) {
          return;
        }
        const data = await response.json();
        if (data && data.data && data.data.images) {
          setFigmaImages(data.data.images);
        }
      } catch (error) {
        // Keep local fallbacks if MCP server is unavailable.
      }
    }

    fetchImageUrls();
  }, []);

  const heroImageUrl = getFigmaImage(figmaImages, FIGMA_IMAGE_NODE_IDS.hero, localFallbacks.hero);
  const sectionImageUrl = getFigmaImage(figmaImages, FIGMA_IMAGE_NODE_IDS.side, localFallbacks.side);
  const featureCards = buildFeatureCards(figmaImages);
  const bottomCards = buildBottomCards(figmaImages);
  const testimonials = buildTestimonials(figmaImages);

  return (
    <div className="page">
      <header className="container navbar">
        <div className="site-name">Site name</div>
        <nav className="nav-right" aria-label="Primary navigation">
          {navLinks.map((label) => (
            <a key={label} href="#" className="nav-link">
              {label}
            </a>
          ))}
          <a href="#" className="button">
            Button
          </a>
        </nav>
      </header>

      <main>
        <section className="container hero">
          <div className="hero-copy">
            <h1>Landing page title</h1>
            <p>
              Subheading that sets up context, shares more info about the website,
              or generally gets people psyched to keep scrolling.
            </p>
            <a href="#" className="button">
              Button
            </a>
          </div>
          <img
            className="hero-image"
            src={heroImageUrl || heroLocal}
            alt="Hero"
            onError={(e) => {
              if (e.currentTarget.src !== heroLocal) e.currentTarget.src = heroLocal;
            }}
          />
        </section>

        <section className="container section">
          <h2>Section heading</h2>
          <div className="cards-3">
            {featureCards.map((card, idx) => (
              <FeatureCard key={card.description + idx} {...card} />
            ))}
          </div>
        </section>

        <section className="container section text-image-section">
          <div className="text-column">
            <h2>Section heading</h2>
            {textBlocks.map((block) => (
              <div key={block.description} className="text-block">
                <h3>{block.title}</h3>
                <p>{block.description}</p>
              </div>
            ))}
            <div className="button-row">
              <a href="#" className="button">
                Button
              </a>
              <a href="#" className="button secondary">
                Secondary button
              </a>
            </div>
          </div>
          <img className="side-image" src={sectionImageUrl} alt="Section" onError={(e)=>{e.currentTarget.src = feature3Local}} />
        </section>

        <section className="container section">
          <h2>Section heading</h2>
          <div className="cards-2">
            {bottomCards.map((card, idx) => (
              <BottomCard key={card.description + idx} {...card} />
            ))}
          </div>
        </section>

        <section className="container testimonial-section">
          <h2>Section heading</h2>
          <div className="testimonial-grid">
            {testimonials.map((testimonial, idx) => (
              <Testimonial key={testimonial.quote + idx} {...testimonial} />
            ))}
          </div>
        </section>

        <section className="cta-section">
          <div className="container cta-inner">
            <h2>Section heading</h2>
            <div className="button-row">
              <a href="#" className="button">
                Button
              </a>
              <a href="#" className="button secondary">
                Secondary button
              </a>
            </div>
          </div>
        </section>
      </main>

      <footer className="container footer">
        <div className="footer-grid">
          <div className="footer-brand">
            <div className="footer-logo">Site name</div>
            <div className="footer-socials">
              <button className="social-icon" aria-label="Twitter">
                <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M22 5.9c-.8.35-1.7.6-2.6.7a4.4 4.4 0 0 0 1.9-2.4 8.8 8.8 0 0 1-2.8 1.1 4.4 4.4 0 0 0-7.4 4 12.5 12.5 0 0 1-9-4.5 4.4 4.4 0 0 0 1.4 5.9 4.4 4.4 0 0 1-2-.6v.1a4.4 4.4 0 0 0 3.5 4.3 4.4 4.4 0 0 1-2 .1 4.4 4.4 0 0 0 4.1 3 8.8 8.8 0 0 1-5.4 1.8A8.9 8.9 0 0 1 2 19.1 12.5 12.5 0 0 0 8.5 21c10.2 0 15.8-8.4 15.8-15.7v-.7A11.3 11.3 0 0 0 22 5.9Z" fill="#000" />
                </svg>
              </button>
              <button className="social-icon" aria-label="Instagram">
                <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M17 2H7a5 5 0 0 0-5 5v10a5 5 0 0 0 5 5h10a5 5 0 0 0 5-5V7a5 5 0 0 0-5-5Z" stroke="#000" strokeWidth="2" />
                  <path d="M12 8.5a3.5 3.5 0 1 1 0 7 3.5 3.5 0 0 1 0-7Z" stroke="#000" strokeWidth="2" />
                  <path d="M17.5 6.5h.01" stroke="#000" strokeWidth="2" strokeLinecap="round" />
                </svg>
              </button>
              <button className="social-icon" aria-label="LinkedIn">
                <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M4 9h4v11H4z" stroke="#000" strokeWidth="2" />
                  <path d="M6 4a2 2 0 1 1 0 4 2 2 0 0 1 0-4Z" stroke="#000" strokeWidth="2" />
                  <path d="M9 14h3v6h-3zM15 14c1.5 0 2.25.75 2.5 1.5V20h-3v-2c0-.5 0-1-.5-1s-1 0-1 1v2h-3v-6h3v.75c.5-.75 1.25-1.5 2.5-1.5Z" stroke="#000" strokeWidth="2" />
                </svg>
              </button>
            </div>
          </div>
          {footerColumns.map((column, idx) => (
            <div key={column.heading + idx} className="footer-col">
              <h4>{column.heading}</h4>
              {column.items.map((item) => (
                <p key={item}>{item}</p>
              ))}
            </div>
          ))}
        </div>
      </footer>
    </div>
  );
}
