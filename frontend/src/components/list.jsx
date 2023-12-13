import React, { useState, useEffect } from 'react';

export default function List() {
    const [listings, setListings] = useState([]);
    useEffect(() => {
        const url = 'http://localhost:8000/api/listings/';

        const fetchTodos = async () => {
            try {
                const response = await fetch(url);
                const data = await response.json();
                console.log(data);
                setListings(data);
            } catch (error) {
                console.log(error);
            }
        };
        fetchTodos()
    }, []);

    return (
        <div>
            <h2>Listings</h2>
            <ul>
                {listings.map((listing) => (
                    <div className="mt-6" key={listing.id} >
                        <div className="max-w-4xl px-10 py-6 bg-white rounded-lg shadow-md">
                            <div className="flex justify-between items-center">
                                <span className="font-light text-gray-600">Jun 1, 2020</span>
                                <a
                                    href={'post/' + listing.id}
                                    className="px-2 py-1 bg-gray-600 text-gray-100 font-bold rounded hover:bg-gray-500"
                                >
                                    Laravel
                                </a>
                            </div>
                            <div className="mt-2">
                                <a href={'post/' + listing.id} className="text-2xl text-gray-700 font-bold hover:underline">
                                    {listing.title}
                                </a>
                                <p className="mt-2 text-gray-600">
                                    {listing.text}
                                </p>
                            </div>
                            <div className="flex justify-between items-center mt-4">
                                <a href={'post/' + listing.id} className="text-blue-500 hover:underline">
                                    Read more
                                </a>
                                <div>
                                    <a href={'post/' + listing.id} className="flex items-center">
                                        <img
                                            src="https://images.unsplash.com/photo-1492562080023-ab3db95bfbce?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=731&q=80"
                                            alt="avatar"
                                            className="mx-4 w-10 h-10 object-cover rounded-full hidden sm:block"
                                        />
                                        <h1 className="text-gray-700 font-bold hover:underline">Alex John</h1>
                                    </a>
                                </div>
                            </div>
                        </div>
                    </div>
                ))}
            </ul>
        </div >
    );
};