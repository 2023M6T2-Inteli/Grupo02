import Registration from "@/components/Registration";
import NewRoute from "@/components/NewRoute";
import SearchBar from "@/components/Search";
import Header from "@/components/Header";
import {useState, useEffect} from "react"
import axios from "axios"

export default function Inspection(){
    const [graphs, setGraphs] = useState([])

    useEffect(() => {

        let url = "http://localhost:8000/graph/get_all"
        
        getGraphs(url)
    })

    const getGraphs = async (url) => {
        const config = {
            headers: {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "GET,PUT,POST,DELETE,PATCH,OPTIONS"
            }}
        const response = await axios(url, config).catch((err) => console.log("Error: ", err))
        //get the data from the response
        const data = response.data
        //set the state of the graphs

        console.log(data)
        setGraphs(data)
    }

    return(
        <div className="bg">
            <Header />
            <div className="flex ml-16 mr-16 mb-16">
                <div className="mt-16 pt-10 pl-10 pb-8 w-2/5 bg-azul rounded-lg">
                    <div className="font-inter text-white">
                        <p>Selecione o espaço confinado que deseja inspecionar.</p>
                    </div>
                    <div className="mt-4">
                        <SearchBar />
                    </div>
                    <div className="mt-6 mb-6">
                        <NewRoute />
                    </div>
                    {graphs.map(json => {
                        return <div className="mt-4 text-primary content-center">
                                    <Registration id = {json.name}/>
                                </div>})}
                </div>

                <div className="grid w-3/5">
                    <div className="ml-16 mt-16 mb-80 bg-azul rounded-lg h-full">
                        <div className="font-inter text-white pt-10 pl-10">
                            <p>Selecione um espaço confinado para visualizar uma prévia de sua rota.</p>
                        </div>
                    </div>
                    <div className="ml-16 mt-24 bg-azul rounded-lg">
                        <div className="font-inter text-white pt-10 pl-10">
                            <p>Iniciar inspeção</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}