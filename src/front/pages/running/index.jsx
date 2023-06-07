import Header from "@/components/Header"

export default function Running() {
    return (
        <div>
            <div className="bg-cinza w-screen h-screen ">
                <Header />
                <div className="flex justify-center items-center flex-col m-4 gap-y-6 text-white">
                    <div className="flex gap-x-6 flex-wrap">
                        <div className="bg-azul rounded-xl p-4">
                            <p>Confira abaixo a trajetória feita pelo robô para realizar a inspeção do espaço selecionado.</p>
                            <img src="" alt="" />
                        </div>
                        <div className="flex gap-y-6 flex-col">
                            <div className="bg-azul rounded-xl p-4 flex justify-center">
                                <p>STATUS</p>
                            </div>
                            <div className="bg-azul flex rounded-xl p-4">
                                <div className="p-2">
                                    <p>22%</p>
                                </div>
                                <div className="p-2">
                                    <img src="https://github.com/2023M6T2-Inteli/Safe-McQueen/blob/Front-end/src/front/public/o2%20(1)%201.png"/>
                                    <p>22%</p>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div className="">
                        <div className="bg-azul p-4 rounded-xl "><p>Logs importantes</p></div>
                    </div>
                </div>
            </div>
        </div>
  
    );
  }





