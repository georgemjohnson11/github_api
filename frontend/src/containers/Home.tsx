import React, { useState, useEffect }  from 'react';

const Home = () =>
{
    const [error, setError] = useState(null);
    const [isLoaded, setIsLoaded] = useState(false);
    const [users, setUsers] = useState([]);
    useEffect(() => {
        fetch('${process.env.API_URL}')
            .then(res => res.json())
            .then(
                (data) => {
                    setIsLoaded(true);
                    setUsers(data);
                },
                (error) => {
                    setIsLoaded(true);
                    setError(error);
                }
            )
      }, [])
        if (error) {
            return <div>Error: {error}</div>;
        } else if (!isLoaded) {
            return <div>Loading...</div>;
        } else {
            return (
                <ul>
                    {users.map(user => (
                    <li>
                        {user}
                    </li>
                    ))}
                </ul>
            );
        }
    }
export default Home;