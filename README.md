# countryfetch

**A CLI tool that fetches information about countries, using https://www.apicountries.com/ for backend.**



## Installation

### Default Way

clone this repository:

```bash
git clone https://github.com/Empester/countryfetch.git
```
cd into the directory:

```bash
cd ./countryfetch
./install.sh
```


If after this your shell cannot find countryfetch, this means you haven't added your local bin to PATH. Either add it to PATH, or make an alias in your .bashrc or .zshrc:

```bash
alias countryfetch="~/.local/bin/countryfetch"
```
> **Note:** The executable you get from compilation can be stored and accessed from anywhere. Using the default way (install.sh), the installer simply runs `deno install --allow-all` and stores the executable in ~/.deno/bin/, which (if you have installed deno) should already be added to PATH, therefore you don't need any aliases. Your shell should be able to detect the command `countryfetch`.

## Usage

```bash
countryfetch <arguments>
```

### Arguments:

- `<country_name>` - Find country information by name.
- `capital <capital>` - Find country to which the specified capital belongs.
- `sync` - Fetches data from API and stores it in `~/.cache/countryfetch/countries.json`. This is done automatically, but can be triggered manually.
  Pass additional argument `sync flags` to fetch and convert flags in ASCII art.
  After syncing flags, every countryfetch command will display flag ASCII art.
- `random` - Get random country information.
- `raw` - Print country information in raw format as JavaScript object.

### Example:

```
$ countryfetch germany

Country: Germany 🇩🇪
Lat/Lng: 51/9
Population: 83,240,525
Languages: German
Capital: Berlin
Capital Lat/Lng: 52.52/13.4
Region: Europe
Subregion: Western Europe
Timezones: UTC+01:00
Top Level Domain: .de
Currencies: Euro [€](EUR)
```

## Flag ASCII Art

[terminal_images](https://github.com/mjrlowe/terminal_images) library is used for image conversion. If you like my project, you should star
this project as well. Maybe contribute and help the author too!

ot read properties of undefined",
you might have an outdated cache. Try running `countryfetch sync` to update the cache.



## Contribution
