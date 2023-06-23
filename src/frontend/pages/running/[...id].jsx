import Header from "@/components/Header"
import { useState, useEffect } from "react"
import Canvas from '@/components/Canvas'

//import roslib
import { 
    RosConnection, 
    ImageViewer, 
    Subscriber, 
    TopicListProvider, 
    useMsg, 
    useTopicList, 
    Publisher, 
    Param, 
    useParam, 
    ParamListProvider, 
    useParamList, 
    ServiceListProvider, 
    useServiceList, 
    ServiceCaller, 
    ServiceServer
} from "rosreact";



export default function Running({id}) {
    useEffect(() => {
        let url = "http://localhost:8000/graph/get_gazebo/"+id
        getAllGraphs(url)
    }, []);
    const [graph, setGraph] = useState([])
    function getAllGraphs(url) {
        fetch(url)
            .then(response => response.json())
            .then(data => {
                setGraph(data)
            })
            .catch(err => {
                console.log(err)
            })
    }
    return (
        <div>
            <RosConnection url={"ws://127.0.0.1:9090"} autoConnect>
                <Publisher 
                        autoRepeat 
                        topic="/connection"
                        throttleRate={10.0} 
                        message={{"data": JSON.stringify(graph)}} 
                        messageType="std_msgs/String"
                    />
            </RosConnection>
            <div className="bg-cinza w-screen h-screen overflow-x-hidden">
                <Header />
                <div className="grid grid-cols-2 grid-rows-2 gap-4 flex items-center text-white mt-6 ml-6 mr-6">
                    {/* Imagem à esquerda */}
                    <div className="border row-span-2 bg-azul rounded-x1 text-center">
                        <p>Confira abaixo a trajetória </p>

                        {/* <Canvas
                            just_show={true}
                            backgroundImageSrc="https://raw.githubusercontent.com/2023M6T2-Inteli/Safe-McQueen/Front-end/src/front/public/Rectangle13.png"
                            alt="Imagem de background para o grafo"
                            className="h-full w-full object-contain"
                        /> */}
                    </div>

                    <div className="border bg-azul flex-wrap rounded-x1 p-4 justify-center">
                        <h1 className="w-full text-center"> STATUS </h1>

                        <div id="turtlebot-status" className="bg-green w-full h-10">
                            <h3 className="h-full flex items-center justify-center">Funcionando</h3>
                        </div>
                    </div>

                    {/* Status e quantidade de gás à direita  */}
                    <div className="border bg-azul rounded-x1 p-4 justify-center grid grid-cols-3">
                        <div className="flex flex-col items-center">
                            <div className="p-2 items-center">
                                <img src="https://raw.githubusercontent.com/2023M6T2-Inteli/Safe-McQueen/Front-end/src/front/public/o2%20(1)%201.png" />
                            </div>
                            <div>
                                <p>22%</p>
                            </div>
                        </div>
                        <div className="flex flex-col items-center">
                            <div className="p-2 flex items-center justify-center flex-col h-full">
                                <img src="https://raw.githubusercontent.com/2023M6T2-Inteli/Safe-McQueen/Front-end/src/front/public/thermometer%201.png" />
                            </div>

                            <div>
                                <p>22%</p>
                            </div>
                        </div>

                        <div className="flex flex-col items-center">
                            <div className="p-2 flex items-center justify-center flex-col h-full">
                                <img style={{ width: '65px' }} src="https://raw.githubusercontent.com/2023M6T2-Inteli/Safe-McQueen/80cc2942e42ec33822c1b5fa39c7f577972cdfbc/src/frontend/public/batery.png" />
                            </div>

                            <div>
                                <p>22%</p>
                            </div>
                        </div>
                    </div>
                </div>
                {/* Logs importantes */}
                <div className="mr-6 ml-6 mt-6">
                    <div className="col-span-2 row-span-1 border bg-azul p-4 rounded-x1 w-full text-white">
                        <h1> Logs importantes </h1>
                        <div className="h-full bg-black">
                            <p className="pl-5">Log</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>

    );
}


export const getServerSideProps = (ctx) =>{
    const {id} = ctx.params
    return {props:{id}}
}
    






