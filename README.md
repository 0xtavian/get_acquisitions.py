# get_free_acquisitions.py
Supply a domain to retrieve the first 10 acquisitions for free. If you get blocked, delete `driver.close() driver.quit()` rerun and solve captcha.

```
python3 get_free_acquisition.py -h
usage: get_free_acquisition.py [-h] [-d D]

Enter Company Name To Query. e.g verizon, gamestop, facebook

optional arguments:
  -h, --help  show this help message and exit
  -d D
```

```
python3 get_free_acquisition.py -d verizon 
Skyward acquired by Verizon Wireless 
SocialRadar acquired by Verizon Wireless 
GTE Corporation acquired by Verizon Wireless 
```

# get_acquisitions.py
Supply a domain to retrieve acquisitions details. [SurfaceBrowser by Security Trails required](https://securitytrails.com/corp/surfacebrowser).

```
python3 get_acquisitions.py --help                                                                          
usage: get_acquisitions.py [-h] [-d D] [-e E] [-p P]

Enter domain name to pull acquisition (-d) from SecurityTrails.com SurfaceBrowser. 
Required arguments: Email Address (-e) and Password (-p)

 arguments:
  -h, --help  show this help message and exit
  -d domain
  -e email
  -p password
  ```

Use [anew](https://github.com/tomnomnom/anew) and [notify](https://github.com/projectdiscovery/notify) to send notifications when new acquisitions occur.

```
while true; do python3 get_acquisitions.py -d hackerone.com -e [redacted] -p [redacted] |\
anew acquisitions.txt | notify; sleep 24h ; done
```  

Example command and results, also saved [here](https://github.com/0xtavian/get_acquisitions.py/blob/main/hackerone.json)
```
python3 get_acquisitions.py -d hackerone.com -e [redacted] -p [redacted] | jq
{
  "records": [
    {
      "acquisition_status": "pending",
      "acquisition_type": "acquisition",
      "announced_on": "2018-01-24",
      "company_name": "Breaker 101",
      "company_permalink": "breaker-101",
      "completed_on": null,
      "domain": "breaker101.com",
      "permalink": "hackerone-acquires-breaker-101--20fbd496"
    }
  ],
  "total": 1
}

```

```
python3 get_acquisitions.py -d hackerone.com -e [redacted] -p [redacted] | jq
{
  "records": [
    {
      "acquisition_status": "complete",
      "acquisition_type": "acquisition",
      "announced_on": "2021-02-16",
      "company_name": "Incubed IT",
      "company_permalink": "incubed-it",
      "completed_on": null,
      "domain": "incubedit.com",
      "permalink": "verizon-communications-acquires-incubed-it--38160e09"
    },
    {
      "acquisition_status": "pending",
      "acquisition_type": "acquisition",
      "announced_on": "2020-10-19",
      "company_name": "Bluegrass Cellular",
      "company_permalink": "bluegrass-cellular",
      "completed_on": null,
      "domain": "bluegrasscellular.com",
      "permalink": "verizon-communications-acquires-bluegrass-cellular--c6e883c6"
    },
    {
      "acquisition_status": "pending",
      "acquisition_type": "acquisition",
      "announced_on": "2020-09-12",
      "company_name": "TracFone Wireless",
      "company_permalink": "tracfone-wireless",
      "completed_on": null,
      "domain": "tracfone.com",
      "permalink": "verizon-communications-acquires-tracfone-wireless--c4da3843"
    },
    {
      "acquisition_status": "complete",
      "acquisition_type": "acquisition",
      "announced_on": "2020-04-16",
      "company_name": "BlueJeans Network",
      "company_permalink": "blue-jeans-network",
      "completed_on": "2020-05-18",
      "domain": "bluejeans.com",
      "permalink": "verizon-communications-acquires-blue-jeans-network--c7b622c1"
    },
    {
      "acquisition_status": "pending",
      "acquisition_type": "acquisition",
      "announced_on": "2019-09-30",
      "company_name": "Jaunt",
      "company_permalink": "jaunt",
      "completed_on": null,
      "domain": "jauntxr.com",
      "permalink": "verizon-communications-acquires-jaunt--60a69924"
    },
    {
      "acquisition_status": "complete",
      "acquisition_type": "acquisition",
      "announced_on": "2019-03-01",
      "company_name": "ProtectWise",
      "company_permalink": "protectwise",
      "completed_on": null,
      "domain": "protectwise.com",
      "permalink": "verizon-communications-acquires-protectwise--24d6cac6"
    },
    {
      "acquisition_status": "complete",
      "acquisition_type": "acquisition",
      "announced_on": "2018-11-16",
      "company_name": "Vidder",
      "company_permalink": "vidder",
      "completed_on": null,
      "domain": "vidder.com",
      "permalink": "verizon-communications-acquires-vidder--a7b069ff"
    },
    {
      "acquisition_status": "pending",
      "acquisition_type": "acquisition",
      "announced_on": "2018-04-19",
      "company_name": "Moment",
      "company_permalink": "moment-3",
      "completed_on": null,
      "domain": "momentdesign.com",
      "permalink": "verizon-communications-acquires-moment-3--325881d5"
    },
    {
      "acquisition_status": null,
      "acquisition_type": null,
      "announced_on": "2018-01-05",
      "company_name": "Niddel",
      "company_permalink": "niddel",
      "completed_on": null,
      "domain": "niddel.com",
      "permalink": "verizon-communications-acquires-niddel--9d2945ad"
    },
    {
      "acquisition_status": "complete",
      "acquisition_type": "acquisition",
      "announced_on": "2017-12-14",
      "company_name": "WideOpenWest - Fiber-Optic Network",
      "company_permalink": "wideopenwest-fiber-optic-network",
      "completed_on": null,
      "domain": null,
      "permalink": "verizon-communications-acquires-wideopenwest-fiber-optic-network--9e76d566"
    },
    {
      "acquisition_status": "complete",
      "acquisition_type": "acquisition",
      "announced_on": "2017-05-11",
      "company_name": "Straight Path Communications",
      "company_permalink": "straight-path-communications",
      "completed_on": "2018-02-28",
      "domain": "spathinc.com",
      "permalink": "verizon-communications-acquires-straight-path-communications--9ddb8570"
    },
    {
      "acquisition_status": "complete",
      "acquisition_type": "acquisition",
      "announced_on": "2016-11-14",
      "company_name": "LQD WiFi",
      "company_permalink": "lqd-wifi",
      "completed_on": null,
      "domain": "lqdwifi.com",
      "permalink": "verizon-communications-acquires-lqd-wifi--9f8c2e09"
    },
    {
      "acquisition_status": "complete",
      "acquisition_type": "acquihire",
      "announced_on": "2016-10-26",
      "company_name": "Vessel",
      "company_permalink": "vessel-2",
      "completed_on": null,
      "domain": "vessel.com",
      "permalink": "verizon-communications-acquires-vessel-2--9a1d56d9"
    },
    {
      "acquisition_status": null,
      "acquisition_type": "acquisition",
      "announced_on": "2016-09-12",
      "company_name": "Sensity Systems",
      "company_permalink": "sensity-systems",
      "completed_on": null,
      "domain": "sensity.com",
      "permalink": "verizon-communications-acquires-sensity-systems--4158962e"
    },
    {
      "acquisition_status": "complete",
      "acquisition_type": "acquisition",
      "announced_on": "2016-08-01",
      "company_name": "FleetMatics",
      "company_permalink": "fleetmatics",
      "completed_on": "2016-11-07",
      "domain": "fleetmatics.com",
      "permalink": "verizon-communications-acquires-fleetmatics--345ce3a3"
    },
    {
      "acquisition_status": "complete",
      "acquisition_type": "acquisition",
      "announced_on": "2016-07-25",
      "company_name": "Yahoo",
      "company_permalink": "yahoo",
      "completed_on": "2017-06-13",
      "domain": "yahoo.com",
      "permalink": "verizon-communications-acquires-yahoo--7ca0cb9e"
    },
    {
      "acquisition_status": "complete",
      "acquisition_type": "acquisition",
      "announced_on": "2016-06-21",
      "company_name": "Telogis",
      "company_permalink": "telogis",
      "completed_on": null,
      "domain": "telogis.com",
      "permalink": "verizon-communications-acquires-telogis--b30f3a3a"
    },
    {
      "acquisition_status": "complete",
      "acquisition_type": "acquisition",
      "announced_on": "2016-04-18",
      "company_name": "Complex",
      "company_permalink": "complex",
      "completed_on": null,
      "domain": "complex.com",
      "permalink": "verizon-communications-acquires-complex--a754cfcf"
    },
    {
      "acquisition_status": "complete",
      "acquisition_type": "acquisition",
      "announced_on": "2016-03-16",
      "company_name": "Volicon",
      "company_permalink": "volicon",
      "completed_on": null,
      "domain": "volicon.com",
      "permalink": "verizon-communications-acquires-volicon--bc041e27"
    },
    {
      "acquisition_status": "complete",
      "acquisition_type": "acquisition",
      "announced_on": "2016-02-22",
      "company_name": "XO Communications",
      "company_permalink": "xo-communications",
      "completed_on": null,
      "domain": "xo.com",
      "permalink": "verizon-communications-acquires-xo-communications--c42b120b"
    },
    {
      "acquisition_status": "complete",
      "acquisition_type": "acquisition",
      "announced_on": "2015-05-12",
      "company_name": "AOL",
      "company_permalink": "aol",
      "completed_on": "2015-06-23",
      "domain": "aol.com",
      "permalink": "verizon-communications-acquires-aol--f95bc697"
    },
    {
      "acquisition_status": null,
      "acquisition_type": null,
      "announced_on": "2014-01-01",
      "company_name": "go90",
      "company_permalink": "go90",
      "completed_on": null,
      "domain": "go90.com",
      "permalink": "verizon-communications-acquires-go90--d53cfbe5"
    },
    {
      "acquisition_status": null,
      "acquisition_type": null,
      "announced_on": "2013-12-09",
      "company_name": "EdgeCast Networks",
      "company_permalink": "edgecast",
      "completed_on": null,
      "domain": "edgecast.com",
      "permalink": "verizon-communications-acquires-edgecast--01e6f6c9"
    },
    {
      "acquisition_status": null,
      "acquisition_type": null,
      "announced_on": "2013-11-13",
      "company_name": "UpLynk",
      "company_permalink": "uplynk",
      "completed_on": null,
      "domain": "uplynk.com",
      "permalink": "verizon-communications-acquires-uplynk--d7fb828a"
    },
    {
      "acquisition_status": null,
      "acquisition_type": null,
      "announced_on": "2012-06-01",
      "company_name": "Hughes Telematics",
      "company_permalink": "hughes-telematics",
      "completed_on": null,
      "domain": "hughestelematics.com",
      "permalink": "verizon-communications-acquires-hughes-telematics--c9f30ef0"
    },
    {
      "acquisition_status": null,
      "acquisition_type": null,
      "announced_on": "2011-08-25",
      "company_name": "CloudSwitch",
      "company_permalink": "cloudswitch",
      "completed_on": null,
      "domain": "cloudswitch.com",
      "permalink": "verizon-communications-acquires-cloudswitch--b6c55bc0"
    },
    {
      "acquisition_status": null,
      "acquisition_type": null,
      "announced_on": "2011-01-27",
      "company_name": "Terremark Worldwide",
      "company_permalink": "terremark-worldwide",
      "completed_on": null,
      "domain": "terremark.com",
      "permalink": "verizon-communications-acquires-terremark-worldwide--e3f2ff57"
    },
    {
      "acquisition_status": null,
      "acquisition_type": null,
      "announced_on": "2008-06-05",
      "company_name": "Alltel",
      "company_permalink": "alltel",
      "completed_on": null,
      "domain": "alltel.com",
      "permalink": "verizon-communications-acquires-alltel--7dc8b060"
    },
    {
      "acquisition_status": "complete",
      "acquisition_type": "acquisition",
      "announced_on": "2006-07-21",
      "company_name": "Inceptor, Inc.",
      "company_permalink": "inceptor",
      "completed_on": null,
      "domain": "inceptor.com",
      "permalink": "verizon-communications-acquires-inceptor--7a864372"
    },
    {
      "acquisition_status": "complete",
      "acquisition_type": "acquisition",
      "announced_on": "2005-03-05",
      "company_name": "Qwest Wireless Spectrum - Network Assets",
      "company_permalink": "qwest-wireless-spectrum-network-assets",
      "completed_on": null,
      "domain": null,
      "permalink": "verizon-communications-acquires-qwest-wireless-spectrum-network-assets--241261b4"
    },
    {
      "acquisition_status": null,
      "acquisition_type": null,
      "announced_on": "2005-02-14",
      "company_name": "MCI",
      "company_permalink": "mci",
      "completed_on": null,
      "domain": "mci.com",
      "permalink": "verizon-communications-acquires-mci--5e49cc86"
    },
    {
      "acquisition_status": "complete",
      "acquisition_type": "acquisition",
      "announced_on": "2000-12-19",
      "company_name": "Verizon Avenue (dba Verizon Enhanced Communities)",
      "company_permalink": "verizon-avenue-dba-verizon-enhanced-communities",
      "completed_on": null,
      "domain": null,
      "permalink": "verizon-communications-acquires-verizon-avenue-dba-verizon-enhanced-communities--f8867213"
    },
    {
      "acquisition_status": "complete",
      "acquisition_type": "acquisition",
      "announced_on": "1998-07-27",
      "company_name": "GTE",
      "company_permalink": "gte",
      "completed_on": "2000-06-30",
      "domain": "gte.com",
      "permalink": "verizon-communications-acquires-gte--fb71e367"
    }
  ],
  "total": 33
}

```
