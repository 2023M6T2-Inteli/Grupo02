import Header from "@/components/Header"
import { useState, useEffect } from "react"
import Canvas from '@/components/Canvas'

export default function Running() {
    const [graph, setGraph] = useState([])


    return (
        <div>
            <div className="bg-black w-screen h-screen">
                <Header />
                <div className="grid grid-cols-2 grid-rows-3 gap-4 flex items-center text-white mt-6 ml-6 mr-6">
                    {/* Imagem à esquerda */}
                    <div className="border row-span-2 bg-azul rounded-x1">
                        <p>Confira abaixo a trajetória </p>
                        <Canvas
                            just_show={true}
                            backgroundImageSrc="https://raw.githubusercontent.com/2023M6T2-Inteli/Safe-McQueen/Front-end/src/front/public/Rectangle13.png"
                            alt="Imagem de background para o grafo"
                        />
                    </div>

                    {/* Status e quantidade de gás à direita  */}
                    <div className="border bg-azul flex rounded-x1 p-4 justify-center">
                        <div className="p-2 flex items-center flex-col">
                            <img src="https://raw.githubusercontent.com/2023M6T2-Inteli/Safe-McQueen/Front-end/src/front/public/o2%20(1)%201.png" />
                            <p>22%</p>
                        </div>
                    </div>

                    <div className="border bg-azul flex rounded-x1 p-4 justify-center">
                        <div className="p-2 flex items-center flex-col">
                            <img src="https://raw.githubusercontent.com/2023M6T2-Inteli/Safe-McQueen/Front-end/src/front/public/thermometer%201.png" />
                            <p>22%</p>
                        </div>
                    </div>

                    {/* Logs importantes */}
                    <div className="col-span-2 row-span-1 border bg-azul p-4 rounded-x1 h-full w-full">
                        <h1> Logs importantes </h1>
                    </div>


                </div>
            </div>
        </div>

    );
}





