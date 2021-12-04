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
            <img src={article.image?article.image:notfoundurl} alt='' className="mr-3 w-24 rounded-xl object-cover"/>
            <h1 className="text-sm flex-1 px-1">{article.title}</h1>
            <div className="px-1 w-8">
                {
                    icon
                }
            </div>
        </div>
    )
}
export default SearchCard
