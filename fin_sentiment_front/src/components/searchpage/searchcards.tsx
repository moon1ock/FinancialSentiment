import React from 'react'
import {ArticleList} from './searchpage'
import SearchCard from './searchcard'
import SentimentCard from './sentimentcard'

const SearchCards = (articles:ArticleList) =>{
    return(
        <div>
            <SentimentCard sentiment={articles.sentiment}/>
            {
                articles.data?
                articles.data.map((article)=>{
                    return <SearchCard {...article} key={article.title}/>
                })
                :null
            }
        </div>
    )
}
export default SearchCards