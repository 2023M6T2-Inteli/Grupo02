import { Search } from "react-bootstrap-icons";

export default function SearchBar(filter) {

    return (
        <>
            <div>
                <div className="bg-gray-50 w-5/6 py-2 pl-2 rounded-full flex justify-between text-primary">
                    <input className="text-sm font-inter w-5/6 pl-4" placeholder="Pesquise por ID do espaço confinado" onChange={filter} />
                    <button className="w-8">
                        <Search />
                    </button>
                </div>
            </div>
        </>
    );
}