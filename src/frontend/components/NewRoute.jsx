import Pop_up_add from "./Pop_up_add";

export default function NewRoute() {
    return(
        <>
        <div className="flex bg-componentes w-5/6 h-12 rounded-lg flex justify-between items-center  text-primary">
            <p className="px-4">Adicionar nova rota</p>
            <Pop_up_add />

        </div>
        </>
    );
}