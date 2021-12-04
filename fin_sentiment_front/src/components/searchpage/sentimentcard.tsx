import React from 'react'
import minus from '../../images/minus.png'
import down from '../../images/down.png'
import up from '../../images/up.png'

const SentimentCard = ({sentiment}:{sentiment:number}) =>{
    let icon = <img src={minus} alt="minus" className="h-8"/>
    if(sentiment < 0)
        icon = <img src={down} alt="down" className="h-8"/>
    if(sentiment > 0)
        icon = <img src={up} alt="up" className="h-8"/>
    return(
        <div className="border border-gray-200 flex items-center my-4 rounded-xl p-2 shadow-xl h-16 justify-center">
            <h1 className="text-xl">Overall Sentiment:</h1>
            <h1 className="text-xl px-2">{Number((sentiment).toFixed(4))}</h1>
            {icon}
        </div>
    )
}
export default SentimentCard