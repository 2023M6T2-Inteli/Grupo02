import { Plus } from "react-bootstrap-icons";

export default function NewRoute() {
    return(
        <>
        <div className="flex pl-2 py-4 pr-6 bg-componentes w-5/6 h-12 rounded-lg flex justify-between text-primary">
            <div className="">
                <p>Adicionar nova rota</p>
            </div>
            <button className="">
                <Plus />
            </button>

        </div>
        </>
    );
}