export default function Insp_H(params) {
    return (
        <>
        <div class="flex bg-white flex-col w-64 items-center rounded-2xl mx-6 mt-10">
            <span class=" mb-8 mt-3 font-semibold">{params.number}</span>
            <span class="mb-8">{params.name}</span>
            <span class="mb-3">{params.data}</span> 
        </div>
        </>
       
    );
}