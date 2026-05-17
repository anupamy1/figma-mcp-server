import React from 'react';
import './LandingPage.css';

const heroImageUrl = 'https://figma-alpha-api.s3.us-west-2.amazonaws.com/images/5ad2c2ba-ae34-4864-9cb8-6cb40b4dbf98';
const featureCardImages = [
  'https://figma-alpha-api.s3.us-west-2.amazonaws.com/images/fd7330c8-0835-4ec3-b905-54c00faafb5b',
  'https://figma-alpha-api.s3.us-west-2.amazonaws.com/images/c8c57764-6b62-40bd-a535-133355afe5e5',
  'https://figma-alpha-api.s3.us-west-2.amazonaws.com/images/ccbd41ab-029f-435a-a139-3fe142a77659'
];
const sectionImageUrl = 'https://figma-alpha-api.s3.us-west-2.amazonaws.com/images/ccbd41ab-029f-435a-a139-3fe142a77659';
const bottomCardImages = [
  'https://figma-alpha-api.s3.us-west-2.amazonaws.com/images/fd7330c8-0835-4ec3-b905-54c00faafb5b',
  'https://figma-alpha-api.s3.us-west-2.amazonaws.com/images/c8c57764-6b62-40bd-a535-133355afe5e5'
];

const navLinks = ['Page', 'Page', 'Page'];
const featureCards = [
  {
    title: 'Subheading',
    description: 'Body text for whatever you’d like to add more to the subheading.',
    image: featureCardImages[0]
  },
  {
    title: 'Subheading',
    description: 'Body text for whatever you’d like to expand on the main point.',
    image: featureCardImages[1]
  },
  {
    title: 'Subheading',
    description: 'Body text for whatever you’d like to share more.',
    image: featureCardImages[2]
  }
];

const textBlocks = [
  {
    title: 'Subheading',
    description: 'Body text for whatever you’d like to expand on the main point.'
  },
  {
    title: 'Subheading',
    description: 'Body text for whatever you’d like to say. Add main takeaway points, quotes, anecdotes.'
  },
  {
    title: 'Subheading',
    description: 'Body text for whatever you’d like to add more to the main point. It provides details, explanations, and context.'
  }
];

const bottomCards = [
  {
    title: 'Subheading',
    description: 'Body text for whatever you’d like to add more to the subheading.',
    image: bottomCardImages[0]
  },
  {
    title: 'Subheading',
    description: 'Body text for whatever you’d like to expand on the main point.',
    image: bottomCardImages[1]
  }
];

const testimonials = [
  {
    quote: '“A terrific piece of praise”',
    name: 'Name',
    description: 'Description'
  },
  {
    quote: '“A fantastic bit of feedback”',
    name: 'Name',
    description: 'Description'
  },
  {
    quote: '“A genuinely glowing review”',
    name: 'Name',
    description: 'Description'
  }
];

const footerColumns = [
  {
    heading: 'Topic',
    items: ['Page', 'Page', 'Page']
  },
  {
    heading: 'Topic',
    items: ['Page', 'Page', 'Page']
  },
  {
    heading: 'Topic',
    items: ['Page', 'Page', 'Page']
  }
];

function FeatureCard({image, title, description}) {
  return (
    <article className="card">
      <img src={image} alt={title} />
      <div>
        <h3>{title}</h3>
        <p>{description}</p>
      </div>
    </article>
  );
}

function BottomCard({image, title, description}) {
  return (
    <article className="card">
      <img src={image} alt={title} />
      <div>
        <h3>{title}</h3>
        <p>{description}</p>
      </div>
    </article>
  );
}

function Testimonial({quote, name, description}) {
  return (
    <article className="testimonial">
      <blockquote className="testimonial-quote">{quote}</blockquote>
      <div className="avatar-row">
        <div className="avatar" aria-hidden="true" />
        <div>
          <div className="avatar-name">{name}</div>
          <div className="avatar-desc">{description}</div>
        </div>
      </div>
    </article>
  );
}

export default function LandingPage() {
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
          <img className="hero-image" src={heroImageUrl} alt="Hero" />
        </section>

        <section className="container section">
          <h2>Section heading</h2>
          <div className="cards-3">
            {featureCards.map((card) => (
              <FeatureCard key={card.description} {...card} />
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
          <img className="side-image" src={sectionImageUrl} alt="Section" />
        </section>

        <section className="container section">
          <h2>Section heading</h2>
          <div className="cards-2">
            {bottomCards.map((card) => (
              <BottomCard key={card.description} {...card} />
            ))}
          </div>
        </section>

        <section className="container testimonial-section">
          <h2>Section heading</h2>
          <div className="testimonial-grid">
            {testimonials.map((testimonial) => (
              <Testimonial key={testimonial.quote} {...testimonial} />
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
          <div className="footer-logo">Site name</div>
          {footerColumns.map((column) => (
            <div key={column.heading} className="footer-col">
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
