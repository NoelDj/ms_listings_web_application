import React, { useEffect, useState } from 'react';


export default function Article(props) {
    const id = props.id
    const [listing, setListing] = useState(null);
    useEffect(() => {
        const url = `${window.location.protocol}//${window.location.hostname}:8000/api/listings/`
        const fetchListing = async () => {
            try {
                const response = await fetch(url);
                if (!response.ok) {
                    throw new Error(`Fetch failed with status ${response.status}`);
                }
                const data = await response.json();
                setListing(data);
            } catch (error) {
                console.error('Error fetching data:', error);
            }
        };

        fetchListing();
    }, [id]);

    return (
        listing && <article>
            <div className="px-4 py-8 md:px-6 md:py-10 lg:py-12 pb-0">
                <div className="mx-auto w-full max-w-3xl">
                    <h1 className="mb-3 text-3xl font-semibold tracking-tighter text-slate-800 md:text-4xl">
                        {listing.title}
                    </h1>
                    <p className="font-serif italic tracking-tighter text-slate-500">
                        Apr 12, 2022
                    </p>
                </div>
            </div>
            <section className="px-4 py-8 md:px-6 md:py-10 lg:py-12">
                <div className="mx-auto w-full max-w-3xl">
                    <div className="font-serif leading-relaxed md:text-xl md:leading-relaxed">
                        <p className="mb-7 last:mb-0">
                            {listing.text}
                        </p>
                    </div>
                </div>
            </section>
        </article>
    )
}
