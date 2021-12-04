import React from 'react'
import {Article} from './searchpage'
import minus from '../../images/minus.png'
import down from '../../images/down.png'
import up from '../../images/up.png'

const SearchCard = (article:Article) =>{
    const notfoundurl = 'https://www.nasdaq.com/sites/acquia.prod/files/image/29525db076bcc42505a356e55dbe94f38b28530b_getty-stock-market-data.jpg?1081762795'
    let icon = <img src={minus} alt="minus" className=""/>
    if(article.sentiment < 0)
        icon = <img src={down} alt="down" className=""/>
    if(article.sentiment > 0)
        icon = <img src={up} alt="up" className=""/>
    return(
        <div className="border border-gray-200 flex items-center my-4 rounded-xl p-2 shadow-xl h-36">
            <img src={article.image?article.image:notfoundurl} alt='' className="mr-3 w-24 md:w-40 rounded-xl object-cover"/>
            <div className="px-1 flex-1 md:flex md:flex-col">
                <h1 className="text-md md:text-lg md:font-bold">{article.title}</h1>
                <h2 className="hidden md:block text-md italic text-gray-500">{article.description}</h2>
            </div>
            <div className="px-1 w-8 md:w-10">
                {
                    icon
                }
            </div>
        </div>
    )
}
export default SearchCard
