import React from 'react'
import {ArticleList} from './searchpage'
import SearchCard from './searchcard'
import SentimentCard from './sentimentcard'

export interface SentimentData{
    sentiment:number
    logo_url:string
    price: number
    prediction: number
    symbol: string
    pricematrix: number[][]
}

const SearchCards = (articles:ArticleList) =>{
    return(
        <div>
            {articles?.data?.length>0?
            <SentimentCard {...{
                sentiment:articles.sentiment,
                logo_url:articles.logo_url,
                price:articles.price,
                prediction:articles.prediction,
                symbol:articles.symbol,
                pricematrix:articles.pricematrix
            }}/>
            :"No results"}
            <div className="md:flex md:flex-wrap md:justify-around">
                {
                    articles.data?
                    articles.data.map((article)=>{
                        return <SearchCard {...article} key={article.title}/>
                    })
                    :null
                }
            </div>
        </div>
    )
}
export default SearchCards