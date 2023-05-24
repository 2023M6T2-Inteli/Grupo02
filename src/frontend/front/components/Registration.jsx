import { Pencil } from "react-bootstrap-icons";

export default function Registration(id) {
    return(
        <>
        <div className="flex pl-2 py-4 pr-6 bg-componentes w-5/6 h-12 rounded-lg flex justify-between">
            <div className="">
                <span>
                    {id.name}
                </span>
            </div>
            <button className="">
                <Pencil />
            </button>

        </div>
        </>
    );
}
