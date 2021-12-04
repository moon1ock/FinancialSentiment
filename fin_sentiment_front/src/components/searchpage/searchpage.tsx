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
            <SearchBar initial={search}/>
            {data.data?
                <SearchCards {...data}/>
                : Array.apply(null, Array(5)).map((val,index)=>{return <CardLoader key={index}/>})
            }
        </div>
    )
}
export default SearchPage
