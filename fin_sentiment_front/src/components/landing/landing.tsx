import React from 'react'
import SearchBar from '../searchbar/searchbar'

const Landing = () => {
    return(
        <div className="h-screen flex flex-col items-center px-2">
            <div className="text-right w-full p-4 pt-32 flex flex-col items-center justify-end">
                <h1 className="text-5xl font-bold my-4"><span className="text-purple-500">Understanding</span> the Market through AI</h1>
                <h1 className="text-xl font-bold my-4">Make <span className="text-purple-500">Cutting-Edge</span> Predictions of the Current Tech Sphere Right Here</h1>
            </div>
            <div className="flex-1 flex w-full">
                <SearchBar initial=''/>
            </div>
        </div>
    )
}
export default Landing;