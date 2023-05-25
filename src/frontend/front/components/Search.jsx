import { Search } from "react-bootstrap-icons";

export default function Searchh() {
    return(
        <>
        <div>
            <div className="bg-gray-50 w-5/6 py-2 pl-2 rounded-full flex justify-between">
                <input className="text-sm font-inter w-2/3 pl-4" placeholder="Pesquise por ID do espaço confinado" />
                <button className="w-8">    
                    <Search />
                </button>
            </div>
        </div>
        </>
    );
}