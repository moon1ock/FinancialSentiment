import React, {useState, useEffect} from 'react'
import {Article} from './searchpage'
import minus from '../../images/minus.png'
import down from '../../images/down.png'
import up from '../../images/up.png'

const SearchCard = (article:Article) =>{
    const [imgurl, setimgUrl] = useState('')
    const notfoundurl = 'https://www.nasdaq.com/sites/acquia.prod/files/image/29525db076bcc42505a356e55dbe94f38b28530b_getty-stock-market-data.jpg?1081762795'
    let icon = <img src={minus} alt="minus" className=""/>
    if(article.sentiment < 0)
        icon = <img src={down} alt="down" className=""/>
    if(article.sentiment > 0)
        icon = <img src={up} alt="up" className=""/>
    useEffect(()=>{
        if(article.image)
            setimgUrl(article.image)
    },[article.image])
    const imageErrorHandler = () =>{
        setimgUrl(notfoundurl)
    }
    return(
        <a href={article.url} rel='noreferrer' target="_blank">
            <div className={`border border-gray-200 flex items-center my-4 md:my-2 rounded-xl p-2 shadow-xl min-h-36 duration-500 md:flex-col md:w-80 md:transform hover:scale-105`}>
                <div className="md:flex md:items-center">
                    <img onError={imageErrorHandler} src={imgurl} alt='' className="mr-3 md:mr-0 w-24 md:w-40 rounded-xl object-cover"/>
                    <div className="hidden md:block w-8 ml-4">
                        {
                            icon
                        }
                    </div>
                    
                </div>
                <div className="px-1 md:my-2 flex-1 md:flex md:flex-col overflow-hidden">
                    <h1 className="text-md md:text-lg md:font-bold ">{article.title}</h1>
                    <h2 className="hidden md:block text-md italic text-gray-500">{article.description}</h2>
                </div>
                <div className="px-1 w-8 md:hidden">
                    {
                        icon
                    }
                </div>
            </div>
        </a>
    )
}
export default SearchCard
