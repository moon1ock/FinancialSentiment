async function getScrapedData(query:string){
    const url = `http://localhost:5000/api/${query}`
    const response = await fetch(url, {
        method: 'GET', // *GET, POST, PUT, DELETE, etc.
      });
    return response.json(); // parses JSON response into native JavaScript objects
    
}
export default getScrapedData