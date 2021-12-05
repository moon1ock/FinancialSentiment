import React, {useEffect, useState} from 'react'
import { useLocation, useNavigate } from 'react-router-dom';
import getScrapedData from '../../adapters/getScrapedData'
import SearchCards from './searchcards'
import SearchBar from '../searchbar/searchbar'
import CardLoader from './cardloader';

export interface Article{
    description: string
    image: string
    pubDate: string
    sentiment: number
    site_name: string
    title: string
    url: string
}

export interface ArticleList{
    data: Article[]
    sentiment: number
    price: number
    logo_url: string
    symbol: string
    prediction: number
    pricematrix: number[][]
}

const SearchPage = () =>{
    const location = useLocation()
    let navigate = useNavigate()
    const [search, setSearch] = useState('')
    const [data, setData] = useState({} as ArticleList)

    //get search state from current url
    useEffect(()=>{
        const query = location.search?.split('=')[1]?.replace('/','')
        if(!query)
            navigate("../", { replace: true });
        setSearch(query)
    },[location.search])

    //once url is set, call api
    useEffect(()=>{
        setData({} as ArticleList)
        if(!search) return
        getScrapedData(search).then(resp=>setData(resp))
    },[search])
    return(
        <div className="p-3">
            <div className="flex items-center md:mr-12">
                <a href="/">
                    <h1 className="hidden shadow-md md:block text-2xl ml-2 border border-purple-500 rounded-xl p-1">
                        Senti<span className="text-purple-500">Predict</span>
                    </h1>
                </a>
                <SearchBar initial={search}/>
            </div>
            {data.data?
                <SearchCards {...data}/>
                : 
                <div className="md:flex md:flex-wrap md:justify-around">
                    {Array.apply(null, Array(10)).map((val,index)=>{return <CardLoader key={index}/>})}
                </div>
            }
        </div>
    )
}
export default SearchPage
