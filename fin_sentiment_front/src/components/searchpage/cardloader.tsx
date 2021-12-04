import React from 'react'

const CardLoader = () =>{
    return(
        <div className="animate-pulse border border-gray-200 flex items-center my-4 rounded-xl p-2 shadow-xl h-36">
            <div className="w-20 h-20 rounded-xl bg-gray-200 mr-3"></div>
            <div className="flex-1 space-y-4 py-1">
            <div className="h-4 bg-gray-400 rounded w-3/4"></div>
            <div className="space-y-2">
                <div className="h-4 bg-gray-400 rounded"></div>
                <div className="h-4 bg-gray-400 rounded w-5/6"></div>
            </div>
            </div>
        </div>
    )
}
export default CardLoader