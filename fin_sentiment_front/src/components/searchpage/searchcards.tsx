import React from 'react'
import {ArticleList} from './searchpage'
import SearchCard from './searchcard'

const SearchCards = (articles:ArticleList) =>{
    return(
        <div>
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