import Registration from "@/components/Registro";
import Search from "@/components/Search";
import Header from "@/components/Header";

export default function Inspection(){
    return(
        <div className="bg">
            <div>
                <Header />
            </div>
            <div className="mt-16 ml-16 pt-10 pl-10 w-1/2 h-96 bg-azul rounded-lg">
                <div className="font-inter text-white">
                    <p>Selecione o espaço confinado que deseja inspecionar.</p>
                </div>
                <div className="mt-4">
                    <Search />
                </div>
                <div className="mt-6">
                    <Registration />
                </div>
            </div>
            <div className="ml-16 mt-16 w-1/2 h-64 bg-azul rounded-lg">
                <div className="font-inter text-white pt-10 pl-10">
                    <p>Selecione um espaço confinado para visualizar uma prévia de sua rota.</p>
                </div>
            </div>
            <div>
            </div>
        </div>
    );
}