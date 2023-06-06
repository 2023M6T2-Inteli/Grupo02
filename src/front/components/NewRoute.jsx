import Pop_up_add from "./Pop_up_add";

export default function NewRoute() {
    return(
        <>
        <div className="flex pl-2 py-4 pr-6 bg-componentes w-5/6 h-12 rounded-lg flex justify-between text-primary">
            <div className="">
                <p>Adicionar nova rota</p>
            </div>
            <button className="">
                <Pop_up_add />
            </button>

        </div>
        </>
    );
}