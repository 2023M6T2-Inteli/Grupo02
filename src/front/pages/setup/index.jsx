import Registration from "@/components/Registration";
import NewRoute from "@/components/NewRoute";
import SearchBar from "@/components/Search";
import Header from "@/components/Header";

var route_id = [
    {
        id: "K2WW0PJN3",
    },
    {
        id: "1KA88J102G",
    },
    {
        id: "0M9KL2S15",
    },
    {
        id: "B6Z11L9M3",
    },
    {
        id: "L099D2FA1M",
    },
]

export default function Inspection(){
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
                    {route_id.map(json => {return <div className="mt-4 text-primary content-center"><Registration id = {json.id} /></div>})}
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