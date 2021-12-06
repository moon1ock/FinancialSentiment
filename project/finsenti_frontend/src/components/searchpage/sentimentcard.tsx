import React, {useState, useEffect} from 'react'
import minus from '../../images/minus.png'
import down from '../../images/down.png'
import up from '../../images/up.png'
import {SentimentData} from './searchcards'
import TimeGraph from './timegraph'

const SentimentCard = ({sentiment, logo_url, price, prediction, symbol, pricematrix,company_name}:SentimentData) =>{
    const [diff, setDiff] = useState(0)
    let icon = <img src={minus} alt="minus" className="h-8"/>
    if(sentiment < 0)
        icon = <img src={down} alt="down" className="h-8"/>
    if(sentiment > 0)
        icon = <img src={up} alt="up" className="h-8"/>
    useEffect(()=>{
        setDiff(Number(((prediction||0)-(price||0)).toFixed(2)))
    },[price, prediction])
    return(
        <div className={`md:mx-4 border border-gray-200 flex items-center my-4 rounded-xl p-2 shadow-xl ${price !== -1?"h-32 md:h-48":"h-16"} justify-center`}>
                {logo_url?<img src={logo_url} alt="" className="h-6 md:h-auto md:max-h-10 mr-3"/>:null}
                <div className="flex flex-col">
                    <h1 className="text-2xl underline font-bold md:mb-2">{company_name} </h1>
                    <div className="flex items-center">
                        <h1 className="text-xl mr-2">Overall Sentiment:</h1>
                        {icon}
                    </div>
                    {
                        price !== -1?
                            <div>
                                <h1>Our Prediction for {symbol}: {Number((prediction).toFixed(2))} ({diff<0?'':'+'}{diff})</h1>
                            </div>:
                        null
                    }
                </div>
                {
                price!==-1
                    ?
                    <div className="ml-3 hidden md:block">
                        <h1 className="text-center underline">3 Month History for {company_name}</h1>
                        <TimeGraph pricematrix={pricematrix}/>
                    </div>:null
                }
                
        </div>
    )
}
export default SentimentCard