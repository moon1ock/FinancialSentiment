import {useEffect, useState} from 'react'
function useLoad(){
    const [loaded, setLoaded] = useState(false);
    useEffect(()=>{
        setLoaded(true)
    },[])
    return {loaded}
}
export default useLoad