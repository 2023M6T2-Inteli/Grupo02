export default function Insp_H({number, name, data}) {
    return (
        <>
        <div className="flex bg-white flex-col w-64 items-center rounded-2xl mx-6 mt-10">
            <span className=" mb-8 mt-3 font-semibold">{number}</span>
            <span className="mb-8">{name}</span>
            <span className="mb-3">{data}</span> 
        </div>
        </>
       
    );
}