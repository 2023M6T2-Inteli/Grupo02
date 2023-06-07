import Header from "@/components/Header"

export default function Running() {
    return (
        <div>
            <div className="bg-cinza w-screen h-screen ">
                <Header />
                <div className="flex justify-center items-center flex-col m-4 gap-y-8 text-white">
                    <div className="flex gap-x-6 flex-wrap">
                        <div className="bg-azul rounded-xl p-4 flex gap-y-2 flex-col">
                            <p className="p-4">Confira abaixo a trajetória feita pelo robô para realizar a inspeção do espaço selecionado.</p>
                            <img src="https://raw.githubusercontent.com/2023M6T2-Inteli/Safe-McQueen/Front-end/src/front/public/Rectangle%2013.png"/>
                        </div>

                        <div className="md-50 flex gap-y-6 flex-col">
                            <div className="bg-azul rounded-xl p-4 flex justify-center ">
                                <p>STATUS</p>
                            </div>
                            <div className="bg-azul flex rounded-xl p-4 justify-center gap-x-4">
                                <div className="p-2 flex items-center flex-col">
                                    <img src="https://raw.githubusercontent.com/2023M6T2-Inteli/Safe-McQueen/Front-end/src/front/public/o2%20(1)%201.png"/>
                                    <p>22%</p>
                                </div>
                                <div className="p-2 flex items-center flex-col gap-y-3.5">
                                    <img src="https://raw.githubusercontent.com/2023M6T2-Inteli/Safe-McQueen/Front-end/src/front/public/thermometer%201.png"/>
                                    <p>22%</p>
                                </div>
                            </div>
                            <div className="">
                                 <div className="bg-azul p-4 rounded-xl h-80 "><p>Logs importantes</p></div>
                            </div> 
                        </div>

                    </div>

                </div>
            </div>
        </div>
  
    );
  }





