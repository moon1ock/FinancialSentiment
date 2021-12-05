import React, {useState, useEffect} from 'react'
import { useNavigate } from 'react-router-dom';

const SearchBar = ({initial}:{initial:string}) =>{
    const [search, setSearch] = useState('');
    useEffect(()=>{setSearch(initial?.replace('%20',' '))},[initial])
    let navigate = useNavigate();
    const changeHandler = (event:React.FormEvent<HTMLInputElement>) =>{
        setSearch(event.currentTarget.value)
    }
    const submitHandler = (event:React.FormEvent) =>{
        event.preventDefault();
        navigate(`../search?query=${search}`, { replace: true });
    }
    return(
        <div className="my-2 p-1 flex-1 md:px-12">
            <form onSubmit={submitHandler} className="flex">
                <input className="md:text-xl flex-1 md:pl-4 p-1 mx-2 border-b-2 border-black outline-none focus:border-blue-500" placeholder="Search For a Company..." type="text" value={search} onChange={changeHandler}/>
            </form>
        </div>
    )
}
export default SearchBar
