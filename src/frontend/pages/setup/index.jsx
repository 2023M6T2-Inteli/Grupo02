import { useState, useEffect } from 'react';
import Registration from "@/components/Registration";
import NewRoute from "@/components/NewRoute";
import SearchBar from "@/components/Search";
import Header from "@/components/Header";
import Canvas from '@/components/Canvas'


export default function Inspection() {
  const [graphs, setGraphs] = useState([])
  const [selectedGraph, setSelectedGraph] = useState('');

  const [id, setId] = useState(null)

  useEffect(() => {

    let url = "http://localhost:8000/graph/get_all"

    getAllGraphs(url)
  }, []);

  const getAllGraphs = async (url) => {

    
    try {
      const all_graphs = await fetch(url); 
        
      const data = await all_graphs.json();

      console.log("A data: ",data)

      setGraphs(data)
      
    } catch (error) {
      console.error('Error get graph:', error);
    }

    

  }

  const handleRouteClick = (imageAddress, name, edges, id) => {
    setId(id)
    setSelectedGraph({
      'image': imageAddress,
      'name': name,
      'edge_': edges
    });
  };
  return (
    <div className="bg bg-cinza w-screen h-screen">
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
          {graphs.map(graph => (
            <div
              key={graph.id}
              className="mt-4 text-primary content-center"
              onClick={() => handleRouteClick(graph.image_address, graph.name, graph.edges, graph.id)}
            >
              <Registration name={graph.name} description={graph.description} id={graph.id} image_address={graph.image_address} />
            </div>
          ))}
        </div>
        <div className="grid w-3/5" >
          <div className="ml-16 mt-16 bg-azul rounded-lg h-full pl-10 pt-2 pr-10">
            <h3 className="text-white text-center">{selectedGraph.name}</h3>
            {console.log("----> ",selectedGraph.edge_)}
            {selectedGraph && (
              <Canvas 
                backgroundImageSrc={selectedGraph.image}
                edge={selectedGraph.edge_}
                alt={selectedGraph.name}  
                just_show={true}
              />
            )}
            {!selectedGraph && (<div className="font-inter text-white pt-10 pl-10">Selecione um espaço confinado para visualizar uma prévia de sua rota.</div>)}
          </div>

          <div className="ml-16 mt-24 bg-azul rounded-lg h-1/2">
            <a href={"running/"+id}>
              <div className="iniciar_inspecao">
                <p className="">Iniciar inspeção</p>
              </div>
            </a>
          </div>
      </div>
    </div>
    </div>
  );
}