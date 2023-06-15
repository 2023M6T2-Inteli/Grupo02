import Header from "@/components/Header"
import { useState, useEffect } from "react"

export default function Running() {
    const [graph, setGraph] = useState([])


    return (
        <div>
            <div className="bg-cinza w-screen h-screen ">
                <Header />
                <div className="flex items-center flex-col m-4 gap-y-8 text-white">
                    {/* Parte de cima, com imagem, status e gás */}
                    <div className="flex gap-x-6 justify-around w-full grid-col-2">
                        {/* Imagem à esquerda */}
                        <div className="pl-10 pr-10 pb-8 w-2/5 bg-azul rounded-lg">
                            <p className="p-4">Confira abaixo a trajetória feita pelo robô para realizar a inspeção do espaço selecionado.</p>
                            <img src="https://raw.githubusercontent.com/2023M6T2-Inteli/Safe-McQueen/Front-end/src/front/public/Rectangle13.png" alt="Imagem de background para o grafo" />
                        </div>

                        {/* Status e quantidade de gás à direita */}
                        <div className="flex gap-y-6 flex-row grid w-3/5 grid-row-2 justify-around">
                            {/* Status */}
                            <div className="bg-azul rounded-xl p-4 flex justify-center">
                                <p>STATUS</p>
                            </div>

                            {/* Quantidade de gás */}
                            <div className="bg-azul flex rounded-xl p-4 justify-center gap-x-4">
                                <div className="p-2 flex items-center flex-col">
                                    <img src="https://raw.githubusercontent.com/2023M6T2-Inteli/Safe-McQueen/Front-end/src/front/public/o2%20(1)%201.png" />
                                    <p>22%</p>
                                </div>
                                <div className="p-2 flex items-center flex">
                                    <img src="https://raw.githubusercontent.com/2023M6T2-Inteli/Safe-McQueen/Front-end/src/front/public/thermometer%201.png" />
                                    <p>22%</p>
                                </div>
                            </div>
                        </div>

                    </div>
                    <div className="w-full pt-10">
                        <div className="bg-azul p-4 rounded-xl h-full  "><p>Logs importantes</p></div>
                    </div>

                </div>
            </div>
        </div>

    );
}





