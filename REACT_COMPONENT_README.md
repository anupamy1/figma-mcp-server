# React Landing Page Component

This folder contains a React component and styling that implements the Figma landing page design.

## Files

- **LandingPage.jsx** - Main React component with all landing page sections
- **LandingPage.css** - Styling for the landing page

## Usage

1. **Import the component** in your React app:
```jsx
import LandingPage from './LandingPage';

function App() {
  return <LandingPage />;
}
```

2. **Make sure to import the CSS** in your main App or wherever you use LandingPage:
```jsx
import './LandingPage.css';
```

## Component Structure

The landing page includes the following sections:

- **Navigation** - Header with site name, page links, and CTA button
- **Hero Section** - Large title, subtitle, and call-to-action button
- **Features Section** - Grid of 3 feature cards with images
- **Content Section** - Alternating content blocks with images
- **Details Section** - Multiple detail items with primary and secondary buttons
- **Testimonials Section** - 3 testimonial cards with quotes and names
- **Footer** - Footer with links and social media icons

## Customization

### Colors
Update color values in `LandingPage.css`:
- Primary color: `#0066cc`
- Background: `#ffffff` and `#f5f5f5`
- Text: `#000000` and `#666666`

### Content
Replace placeholder text in `LandingPage.jsx` with your actual content:
- Section headings
- Feature descriptions
- Testimonial quotes
- Footer links

### Images
Replace the placeholder div elements with actual image components:
```jsx
// Instead of:
<div className="card-image" style={{ backgroundColor: '#e0e0e0', height: '300px' }}></div>

// Use:
<img src="your-image.jpg" alt="Feature image" className="card-image" />
```

### Responsive Design
The component includes responsive styles for mobile devices (media query for screens under 768px).

## Installation

If using npm packages like `npm install react`, make sure to have React 17+ installed.

## Browser Support

Modern browsers (Chrome, Firefox, Safari, Edge) with ES6 support.
