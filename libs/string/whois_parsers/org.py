parser = {
  "creation_date": [ "\nCreated On: \s?(.+)", "" ], 
  "domain_name": [ "Domain Name: \s?(.+)", "" ], 
  "expiration_date": [ "Registry Expiry Date: \s*(.+)", "" ], 
  "name_servers": [ "Name Server: \s?(.+)\s*", "" ], 
  "registrant": [ "Registrant Name: \s*(.+)", "" ], 
  "registrar": [ "Registrar: \s?(.+)", "" ], 
  "status": [ "Status: \s?(.+)", "" ], 
  "updated_date": [ "\nLast Updated On: \s?(.+)", "" ]
}