
<h1 align="center">
  <a>Financial Sentiment Based on News</a>
</h1>

<h2>
  Project Organization
</h2>

------------

    ├── README.md          <- The top-level README for developers using this project.
    ├── docs               <- Assignment Deliverables
    │
    ├── src                <- Code for Flask Backend
    │   ├── templates      <- HTML templates used for testing
    │   ├── main_Google.py <- Script for Backend
    │   └── requirements.txt            
    │
    │
    └── fin_sentiment_front <- React Project Containing Frontend code
        │
        ├── src           
        │   └── adapters   <- Functions with API Calls
        │   └── components <- JSX Components that make up the site
        │   └── hooks      <- Any Custom Hooks for the app
        │   └── images     <- Images and Icons for the site
        │   └── App.tsx    <- Central component for App
        │
        ├── tailwind.config.js <- Config file for tailwind
        ├── tsconfig.json      <- Config files for typescript
        └── package.json       <- Node packages used to make app
   

--------

<h2> 
  Using the Frontend
</h2>

<p>
  The frontend of the project uses Node 14.17.5, TypeScript 4.5.2, React 17.0.2, and Tailwind 2.2.17, initialized with create-react-app
  
  Change you directory to fin_sentiment_front and run `npm install` to install dependencies
  
  To start, run `npm run start` and visit `localhost:3000` to see the landing page
  Searches have the url `/search?query={query}`
</p>
