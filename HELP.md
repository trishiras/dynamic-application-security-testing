## SAMPLE ZAPROXY YAML CONFIGURATION FILE



```


---
env:                                   # The environment, mandatory
  contexts :                           # List of 1 or more contexts, mandatory
    - name: context 1                  # Name to be used to refer to this context in other jobs, mandatory
      urls: [URL]                           # A mandatory list of top level urls, everything under each url will be included
      includePaths:                    # An optional list of regexes to include
      excludePaths:                    # An optional list of regexes to exclude
      authentication:                  # TBA: In time to cover all auth configs
  vars:                                # List of 1 or more variables, can be used in urls and selected other parameters
  parameters:
    failOnError: true                  # If set exit on an error
    failOnWarning: false               # If set exit on a warning
    progressToStdout: true             # If set will write job progress to stdout

jobs:
  - type: addOns                       # Add-on management
    parameters:
     updateAddOns: true               # Update any add-ons that have new versions
    install:                           # A list of non standard add-ons to install from the ZAP Marketplace
    uninstall:                         # A list of standard add-ons to uninstall
  - type: passiveScan-config           # Passive scan configuration
    parameters:
      maxAlertsPerRule: 10             # Int: Maximum number of alerts to raise per rule
      scanOnlyInScope: true            # Bool: Only scan URLs in scope (recommended)
      maxBodySizeInBytesToScan:        # Int: Maximum body size to scan, default: 0 - will scan all messages
  - type: graphql                      # GraphQL definition import
    parameters:
      endpoint:                        # String: the endpoint URL, default: null, no schema is imported
  - type: openapi                      # OpenAPI definition import
    parameters:
      apiFile:                         # String: Local file containing the OpenAPI definition, default: null, no definition will be imported
      apiUrl:                          # String: URL containing the OpenAPI definition, default: null, no definition will be imported
      targetUrl:                       # String: URL which overrides the target defined in the definition, default: null, the target will not be overriden
  - type: soap                         # SOAP WSDL import
    parameters:
      wsdlFile:                        # String: Local file path of the WSDL, default: null, no definition will be imported
      wsdlUrl:                         # String: URL pointing to the WSDL, default: null, no definition will be imported
  - type: spider                       # The traditional spider - fast but doesnt handle modern apps so well
    parameters:
      context:                         # String: Name of the context to spider, default: first context
      url:                             # String: Url to start spidering from, default: first context URL
      maxDuration: 30                    # Int: The max time in minutes the spider will be allowed to run for, default: 0 unlimited
      maxDepth:                        # Int: The maximum tree depth to explore
      maxChildren:                     # Int: The maximum number of children to add to each node in the tree
  - type: spiderAjax                   # The ajax spider - slower than the standard spider but handles modern apps well
    parameters:
      context:                         # String: Name of the context to spider, default: first context
      url:                             # String: Url to start spidering from, default: first context URL
      maxDuration: 30                    # Int: The max time in minutes the ajax spider will be allowed to run for, default: 0 unlimited
      maxCrawlDepth:                   # Int: The max depth that the crawler can reach, default: 10, 0 is unlimited
      numberOfBrowsers:                # Int: The number of browsers the spider will use, more will be faster but will use up more memory, default: 1
  - type: passiveScan-wait             # Passive scan wait for the passive scanner to finish
    parameters:
      maxDuration:                   # Int: The max time to wait for the passive scanner, default: 0 unlimited
  - type: activeScan                   # The active scanner - this actively attacks the target so should only be used with permission
    parameters:
      context:                         # String: Name of the context to attack, default: first context
      policy:                          # String: Name of the scan policy to be used, default: Default Policy
      maxRuleDurationInMins:           # Int: The max time in minutes any individual rule will be allowed to run for, default: 0 unlimited
      maxScanDurationInMins: 60          # Int: The max time in minutes the active scanner will be allowed to run for, default: 0 unlimited
  - type: report                       # Report generation
    parameters:
      template:  "modern"                       # String: The template id, default : modern
      theme:                           # String: The template theme, default: the first theme defined for the template (if any)
      reportDir: "path"                      # String: The directory into which the report will be written
      reportFile: "reportname"
      reportTitle: "reportTitle"           # String: The report title
      reportDescription:               # String: The report description


```



## ZAProxy -help command output.


```
Usage:
        zap.sh [Options]
Core options:
        -version                 Reports the ZAP version
        -cmd                     Run inline (exits when command line options complete)
        -daemon                  Starts ZAP in daemon mode, i.e. without a UI
        -config <kvpair>         Overrides the specified key=value pair in the configuration file
        -configfile <path>       Overrides the key=value pairs with those in the specified properties file
        -dir <dir>               Uses the specified directory instead of the default one
        -installdir <dir>        Overrides the code that detects where ZAP has been installed with the specified directory
        -h                       Shows all of the command line options available, including those added by add-ons
        -help                    The same as -h
        -newsession <path>       Creates a new session at the given location
        -session <path>          Opens the given session after starting ZAP
        -lowmem                  Use the database instead of memory as much as possible - this is still experimental
        -experimentaldb          Use the experimental generic database code, which is not surprisingly also still experimental
        -nostdout                Disables the default logging through standard output
        -loglevel <level>        Sets the log level, overriding the values specified in the log4j2.properties file in the home directory
        -sbomzip <path>          Creates a zip file containing all of the available SBOMs
        -suppinfo                Reports support info to the command line and exits
        -silent                  Ensures ZAP does not make any unsolicited requests, including check for updates
Add-on options:
        -addoninstall <addOnId>   Installs the add-on with specified ID from the ZAP Marketplace
        -addoninstallall          Install all available add-ons from the ZAP Marketplace
        -addonuninstall <addOnId> Uninstalls the Add-on with specified ID
        -addonupdate              Update all changed add-ons from the ZAP Marketplace
        -addonlist                List all of the installed add-ons
        -certload <path>         Loads the Root CA certificate from the specified file name
        -certpubdump <path>      Dumps the Root CA public certificate into the specified file name, this is suitable for importing into browsers
        -certfulldump <path>     Dumps the Root CA full certificate (including the private key) into the specified file name, this is suitable for importing into ZAP
        -host <host>             Overrides the host of the main proxy, specified in the configuration file
        -port <port>             Overrides the port of the main proxy, specified in the configuration file
        -quickurl <target url>   The URL to attack, e.g. http://www.example.com
        -quickout <filename>     The file to write the HTML/JSON/MD/XML results to (based on the file extension)
        -quickprogress:          Display progress bars while scanning
        -zapit <target url>      The URL to perform a quick 'reconnaissance' scan on, e.g. http://www.example.com The -cmd option must be specified
        -graphqlfile <path>       Imports a GraphQL Schema from a File
        -graphqlurl <url>         Imports a GraphQL Schema from a URL
        -graphqlendurl <url>      Sets the Endpoint URL
        -openapifile <path>      Imports an OpenAPI definition from the specified file name
        -openapiurl <url>        Imports an OpenAPI definition from the specified URL
        -openapitargeturl <url>  The Target URL, to override the server URL present in the OpenAPI definition. Refer to the help for supported format.
        -script <script>         Run the specified script from commandline or load in GUI
        -notel                   Turns off telemetry calls
        -autorun <source>        Run the automation jobs specified in the file or from the URL
        -autogenmin <filename>   Generate template automation file with the key parameters
        -autogenmax <filename>   Generate template automation file with all parameters
        -autogenconf <filename>  Generate template automation file using the current configuration
        -hud                     Launches a browser configured to proxy through ZAP with the HUD enabled, for use in daemon mode
        -hudurl <url>            Launches a browser as per the -hud option with the specified URL
        -hudbrowser <browser>    Launches a browser as per the -hud option with the specified browser, supported options: Chrome, Firefox by default Firefox
        -postmanfile <path>          Imports a Postman collection from the specified file name.
        -postmanurl <url>            Imports a Postman collection from the specified URL.
        -postmanendpointurl <url>    The endpoint URL, to override the base URLs present in the Postman collection.
```