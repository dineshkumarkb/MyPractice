from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_setup import Base,Restaurant,MenuItem
import cgi


engine = create_engine('sqlite:///restaurantmenun.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

def main():
    try:
        port = 8080
        server = HTTPServer(('',port),WebServerHandler)
        print " Server Running on port %s " % port
        server.serve_forever()



    except KeyboardInterrupt:
        print "Ctrl+C is pressed"
        server.socket.close()


class WebServerHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        try:
            if self.path.endswith('/hello'):
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()

                output = '<html><body>Hello there</body></html>'
                self.wfile.write(output)
                print output
                return

            if self.path.endswith("/restaurants/new"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = ""
                output += "<html><body>"
                output += "<h1>Make a New Restaurant</h1>"
                output += "<form method = 'POST' enctype='multipart/form-data' action = '/restaurants/new'>"
                output += "<input name = 'newRestaurantName' type = 'text' placeholder = 'New Restaurant Name' > "
                output += "<input type='submit' value='Create'>"
                output += "</form></body></html>"
                self.wfile.write(output)
                return

            if self.path.endswith('/edit'):
                restaurantIDPath = self.path.split("/")[2]
                restaurant_query = session.query(Restaurant).filter_by(id=restaurantIDPath).one()
                if restaurant_query:
                    self.send_response(200)
                    self.send_header('Content-type','text/html')
                    self.end_headers()
                    output = "<html><title>Edit_Restaurant</title><body>EditPage</br>"
                    output += "<h1>"
                    output += restaurant_query.name
                    output += "</h1>"
                    output += "<form method='POST' enctype='multipart/form-data' action = '/restaurants/%s/edit' >" % restaurantIDPath
                    output += "<input name = 'editRestaurantName' type='text' placeholder = '%s' >" % restaurant_query.name
                    output += "<input type = 'submit' value = 'Rename'>"
                    output += "</form>"
                    output += "</body></html>"

            if self.path.endswith('/restaurants'):
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                myquery = session.query(Restaurant).all()
                output = '<html><body><div class=container><a href="/restaurants/new">Make new restaurant</a></br></br>'
                for q in myquery:
                    output+=q.name
                    output += '</br>'
                    output+='<a href="/restaurants/%s/edit">Edit</a>' % q.id
                    output+='</br>'
                    output+='<a href="#">Delete</a>'
                    output+='</br></body></html>'
                self.wfile.write(output)
                return

        except IOError:
            self.send_error(404, "File not found", self.path)

    def do_POST(self):
            try:
                if self.path.endswith("/restaurants/new"):
                    ctype, pdict = cgi.parse_header(
                        self.headers.getheader('content-type'))
                    print ctype,pdict
                    if ctype == 'multipart/form-data':
                        fields = cgi.parse_multipart(self.rfile, pdict)
                        messagecontent = fields.get('newRestaurantName')
                        print messagecontent
                        # Create new Restaurant Object
                        newRestaurant = Restaurant(name=messagecontent[0])
                        session.add(newRestaurant)
                        session.commit()

                        self.send_response(301)
                        self.send_header('Content-type', 'text/html')
                        self.send_header('Location', '/restaurants')
                        self.end_headers()

                if self.path.endswith("/edit"):
                    ctype,pdict = cgi.parse_header(self.headers.getheaders('content-type'))
                    if ctype == 'multipart/form-data':
                        fields = cgi.parse_multipart(self.rfile,pdict)
                        messagecontent = fields.get('editRestaurantName')
                        restaurantIDPath = self.path.split("/")[2]

                        myRestaurantQuery = session.query(Restaurant).filter_by(
                            id=restaurantIDPath).one()
                        if myRestaurantQuery != []:
                            myRestaurantQuery.name = messagecontent[0]
                            session.add(myRestaurantQuery)
                            session.commit()
                            self.send_response(301)
                            self.send_header('Content-type', 'text/html')
                            self.send_header('Location', '/restaurants')
                            self.end_headers()


            except:
                pass











if __name__ == "__main__":
    main()
