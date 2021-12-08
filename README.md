
<h1 align="center">
  <a>Financial Sentiment Based on News</a>
</h1>

<video controls loop>
  <video src="https://github.com/moon1ock/FinancialSentiment/blob/main/readme_support/demo.gif?raw=true" width="1024"/>
</video>

## Tutorial

- Use this application to gauge the latest relevant news articles about any company of your interest.
- You may search by the **listed company name** (e.g.`Alphabet Inc.`), **common name** (e.g. `Google`), ticker (e.g. `GOOGL`), or _even_ have a typo in the query (e.g. `Gogle`).
    - we use special APIs to map your request to the traded ticker and make sure to retrieve the latest and the most relevant _stock_ _and_ news data.   
    - the way you spell the company **will not** affect your search results.
- You can also send requests directly to our API ([refer to the backend](https://github.com/moon1ock/FinancialSentiment/blob/main/project/finsenti_backend/README.md)) and parse the JSON file with the news, stock data, and sentiment yourself.
- We get data from 1800+ reputable news sources and organize them with regard to importance and relevancy so that you don't have to!

## Components

### API

There is a separate server that acts as an API. The server is built with Flask. For more efficient responses multi-threading and cache are used.
[Refer to the Backend README](https://github.com/moon1ock/FinancialSentiment/blob/main/project/finsenti_backend/README.md)

### React

User interface is built with React and Tailwind with an elegant and minimalist design delivering a clear and pleasant experience to the user.
[Refer to the Frontend README](https://github.com/moon1ock/FinancialSentiment/blob/main/project/finsenti_frontend/README.md)


## Usage

1. Follow the instructions for staring the [API](https://github.com/moon1ock/FinancialSentiment/blob/main/project/finsenti_backend/README.md)
2. Follow the instructions for staring the [FrontEnd](https://github.com/moon1ock/FinancialSentiment/blob/main/project/finsenti_frontend/README.md)
3. You may access the server at `localhost:5000`.

## Project Organization


------------

    ├── README.md          <- The top-level README for developers using this project.
    |
    ├── docs               <- Assignment Deliverables          
    │
    ├── test               <- Tests for Project           
    │
    └── project <- Project Code for Front and Backend
        |
        ├──finsenti_backend
        |   |
        |   └──src                 <- Code for Flask Backend
        |     |
        |     ├── templates        <- HTML templates used for testing
        |     ├── main.py   <- Script for Backend
        |     └── requirements.txt <- Required Packages to Run Backend
        │
        └──finsenti_frontend     
              |
              ├── src            <- Code for React Frontend
              |   |
              |   ├── adapters   <- Functions with API Calls
              |   ├── components <- JSX Components that make up the site
              |   ├── hooks      <- Custom Hooks for the app
              |   ├── images     <- Images and Icons for the site
              |   └── App.tsx    <- Central component for App
              │
              ├── tailwind.config.js <- Config file for tailwind
              ├── tsconfig.json      <- Config files for typescript
              └── package.json       <- Node packages used to make app
   

--------


