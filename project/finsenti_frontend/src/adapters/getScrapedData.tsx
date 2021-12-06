async function getScrapedData(query:string){
    const url = `http://localhost:5000/api/${query}`
    const response = await fetch(url, {
        method: 'GET',
      });
    return response.json();
    
}
export default getScrapedData
