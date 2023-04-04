<h2>Description:</h2>

<p>Kvartoblik - apartment accounting and display system.

This is an api for a platform for developers. You can place information about the houses on it: the number of sections, floors, apartments, the cost of each apartment. The platform shows which apartments are available for purchase, as well as a detailed description of each apartment.

Such platform previously existed, but at the moment the project is closed. I still have access to the design of this platform and I decided to write an api for it. I think such platform would be very useful for developers, so that their clients can visually get acquainted with the developer's buildings and choose an apartment for purchase. I believe that such platform will increase the sales of any residential complex.
Link to design https://www.behance.net/gallery/67993249/Kvartoblik-sistema-ucheta-i-demonstracii-kvartir
</p>


<h2>Project details:</h2>

Residential complex. Input data about the object under construction: its name, address, description.
<br>http://localhost:8000/projectcreate/
<br>http://localhost:8000/project/

Buildings and sections. Here you can enter the buildings that will be built in the residential complex and sections in each building.
<br>http://localhost:8000/buildingcreate/
<br>http://localhost:8000/building/

Layouts. At this stage, standard layouts of apartments are added, and an explication for all residential premises.
<br>http://localhost:8000/layoutcreate/
<br>http://localhost:8000/layout/

Floor plan creation. At this stage, apartment layouts are assigned to each floor. After that, “apartment” objects will be automatically created and each apartment will be assigned the status “for sale”
<br>http://localhost:8000/floorplan/

Price. The last stage of creating an apartment accounting. Here you enter: floor section, cost per square meter, floor cost coefficient, room cost coefficient.
According to the formula price per square meter * (coefficient of floor + coefficient of room), a price is assigned for each apartment on the floor.
<br>http://localhost:8000/apartmentsale/

<h2>Running the Project</h2>
<ul>
<li>Install the requirements:</li>
<ul><li>pip install -r requirements.txt</li></ul>

<li>Apply the migrations:</li>
<ul>
<li>python manage.py makemigrations</li>
<li>python manage.py migrate</li>
</ul>

<li>Create Super User:</li>
<ul>
<li>python manage.py createsuperuser</li>
</ul>

<li>Finally, run the development server:</li>
<ul>
<li>python manage.py runserver</li>
</ul>
</ul>










