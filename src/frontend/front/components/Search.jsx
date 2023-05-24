import { Search } from "react-bootstrap-icons";

export default function Searchh() {
    return(
        <>
        <div>
            <div className="bg-gray-50 w-5/6 py-2 pl-2 rounded-full flex justify-between">
                <input className="text-sm w-2/3" placeholder="Pesquise por ID do espaço confinado" />
                <button className="w-8">    
                    <Search />
                </button>
            </div>
            {/* <div className="justify-between group flex items-center bg-blue-200 max-w-xs rounded-full">
                <input className="w-64 focus:ring-2 focus:ring-blue-500 focus:outline-none appearance-none text-sm leading-6 text-slate-900 placeholder-slate-400 rounded-md py-2 pl-10 ring-1 ring-slate-200 shadow-sm border-none bg-transparent" type="text" aria-label="Filter projects" placeholder="Pesquise por ID do espaço confinado"></input>
                <svg width="20" height="20" fill="currentColor" class="flex justify-center right-3 top-1/2 -mt-2.5 text-slate-400 pointer-events-none group-focus-within:text-blue-500 pr-10" aria-hidden="true">
                    <path fill-rule="evenodd" clip-rule="evenodd" d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z" />
                </svg>
            </div> */}
        </div>
        </>
    );
}