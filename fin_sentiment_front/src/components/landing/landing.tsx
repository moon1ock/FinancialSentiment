import React, {useEffect, useState} from 'react'
import SearchBar from '../searchbar/searchbar'

const Landing = () => {
    const [text, setText] = useState('');
    const [finished, setFinished] = useState(false)
    const textlist = ['Analyzing','Shifting','Shaping']
    const textparts:string[] = []
    for(let i=0; i<textlist.length; i++){
        let curr=""
        for(const letter of textlist[i]){
            curr+=letter
            textparts.push(curr);
        }
        for(let j=0; j<2; j++){
            textparts.push(curr);
        }
        if(i!==textlist.length-1){
            for(const letter of textlist[i]){
                curr = curr.slice(0,curr.length-1)
                textparts.push(curr);
            }
        }
    }
    useEffect(()=>{
        for(let i=0; i<textparts.length;i++){
            setTimeout(() => {
                setText(textparts[i]);
                if(i===textparts.length-1)
                    setFinished(true)
            }, i*150);
        }
    },[])
    return(
        <div className={`h-screen flex flex-col items-center px-2 md:justify-center duration-1000 ${finished?'':''}`}>
            <div className="text-right w-full p-4 pt-32 md:pt-0 flex flex-col items-center justify-end flex-1">
                <h1 className={`text-5xl font-bold my-4 w-full md:text-6xl`}><span className="text-purple-500">{text}</span> the Market through AI</h1>
                <h1 className={`text-xl font-bold my-4 w-full`}>Make <span className="text-purple-500">Cutting-Edge</span> Predictions of the Current Tech Sphere</h1>
            </div>
            <div className="flex-1 flex w-full">
                <SearchBar initial=''/>
            </div>
        </div>
    )
}
export default Landing;