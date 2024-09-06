# shellcheck shell=bash disable=SC2148
# File auto-generated by completionFinder.py, do not modify manually

function_exists() {
    declare -f -F "$1" > /dev/null
    return $?
}

# Checks that bash-completion is recent enough
function_exists _get_comp_words_by_ref || return 0

_gdal2tiles.py()
{
  local cur prev
  COMPREPLY=()
  _get_comp_words_by_ref cur prev
  case "$cur" in
    -*)
      key_list=""
      mapfile -t COMPREPLY < <(compgen -W "$key_list" -- "$cur")
      return 0
      ;;
  esac
  return 0
}
complete -o default -F _gdal2tiles.py gdal2tiles.py
_gdal2xyz.py()
{
  local cur prev
  COMPREPLY=()
  _get_comp_words_by_ref cur prev
  case "$cur" in
    -*)
      key_list="-h -skip -srcwin -b -allbands -csv -skipnodata -srcnodata -dstnodata "
      mapfile -t COMPREPLY < <(compgen -W "$key_list" -- "$cur")
      return 0
      ;;
  esac
  return 0
}
complete -o default -F _gdal2xyz.py gdal2xyz.py
_gdaladdo()
{
  local cur prev
  COMPREPLY=()
  _get_comp_words_by_ref cur prev
  case "$cur" in
    -*)
      key_list="-r -ro -clean -q -oo -minsize --help-general --version --build --license --formats --format --optfile --config --debug --pause --locale "
      mapfile -t COMPREPLY < <(compgen -W "$key_list" -- "$cur")
      return 0
      ;;
  esac
  tool=${COMP_WORDS[0]}
  case "$prev" in
    --format)
      key_list="$( $tool --formats | tail -n +2 | cut -f 3 -d ' ')"
      mapfile -t COMPREPLY < <(compgen -W "$key_list" -- "$cur")
      ;;
  esac
  return 0
}
complete -o default -F _gdaladdo gdaladdo
_gdalbuildvrt()
{
  local cur prev
  COMPREPLY=()
  _get_comp_words_by_ref cur prev
  case "$cur" in
    -*)
      key_list="-tileindex -resolution -te -tr -tap -separate -b -sd -allow_projection_difference -q -addalpha -hidenodata -srcnodata -vrtnodata -ignore_srcmaskband -a_srs -r -oo -input_file_list -overwrite -strict -non_strict "
      mapfile -t COMPREPLY < <(compgen -W "$key_list" -- "$cur")
      return 0
      ;;
  esac
  return 0
}
complete -o default -F _gdalbuildvrt gdalbuildvrt
_gdal_calc.py()
{
  local cur prev
  COMPREPLY=()
  _get_comp_words_by_ref cur prev
  case "$cur" in
    -*)
      key_list="--help --calc -a --a_band -b --b_band -c --c_band -d --d_band -e --e_band -f --f_band -g --g_band -h --h_band -i --i_band -j --j_band -k --k_band -l --l_band -m --m_band -n --n_band -o --o_band -p --p_band -q --q_band -r --r_band -s --s_band -t --t_band -u --u_band -v --v_band -w --w_band -x --x_band -y --y_band -z --z_band -A --A_band -B --B_band -C --C_band -D --D_band -E --E_band -F --F_band -G --G_band -H --H_band -I --I_band -J --J_band -K --K_band -L --L_band -M --M_band -N --N_band -O --O_band -P --P_band -Q --Q_band -R --R_band -S --S_band -T --T_band -U --U_band -V --V_band -W --W_band -X --X_band -Y --Y_band -Z --Z_band --outfile --NoDataValue --hideNoData --type --format --creation-option --allBands --overwrite --debug --quiet --color-table --extent --projwin --projectionCheck --calc, --outfile "
      mapfile -t COMPREPLY < <(compgen -W "$key_list" -- "$cur")
      return 0
      ;;
  esac
  tool=${COMP_WORDS[0]}
  case "$prev" in
    -f)
      key_list="$( $tool --formats | tail -n +2 | cut -f 3 -d ' ')"
      mapfile -t COMPREPLY < <(compgen -W "$key_list" -- "$cur")
      ;;
    --format)
      key_list="$( $tool --formats | tail -n +2 | cut -f 3 -d ' ')"
      mapfile -t COMPREPLY < <(compgen -W "$key_list" -- "$cur")
      ;;
  esac
  return 0
}
complete -o default -F _gdal_calc.py gdal_calc.py
_gdalchksum.py()
{
  local cur prev
  COMPREPLY=()
  _get_comp_words_by_ref cur prev
  case "$cur" in
    -*)
      key_list=""
      mapfile -t COMPREPLY < <(compgen -W "$key_list" -- "$cur")
      return 0
      ;;
  esac
  return 0
}
complete -o default -F _gdalchksum.py gdalchksum.py
_gdalcompare.py()
{
  local cur prev
  COMPREPLY=()
  _get_comp_words_by_ref cur prev
  case "$cur" in
    -*)
      key_list=""
      mapfile -t COMPREPLY < <(compgen -W "$key_list" -- "$cur")
      return 0
      ;;
  esac
  return 0
}
complete -o default -F _gdalcompare.py gdalcompare.py
_gdal-config()
{
  local cur prev
  COMPREPLY=()
  _get_comp_words_by_ref cur prev
  case "$cur" in
    -*)
      key_list="--prefix --libs --dep-libs --cflags --datadir --version --ogr-enabled --gnm-enabled --formats "
      mapfile -t COMPREPLY < <(compgen -W "$key_list" -- "$cur")
      return 0
      ;;
  esac
  return 0
}
complete -o default -F _gdal-config gdal-config
_gdal_contour()
{
  local cur prev
  COMPREPLY=()
  _get_comp_words_by_ref cur prev
  case "$cur" in
    -*)
      key_list="-b -a -amin -amax -3d -inodata -snodata -f -i -dsco -lco -off -fl -e -nln -q -p "
      mapfile -t COMPREPLY < <(compgen -W "$key_list" -- "$cur")
      return 0
      ;;
  esac
  return 0
}
complete -o default -F _gdal_contour gdal_contour
_gdaldem()
{
  local cur prev
  COMPREPLY=()
  _get_comp_words_by_ref cur prev
  case "$cur" in
    -*)
      key_list=""
      mapfile -t COMPREPLY < <(compgen -W "$key_list" -- "$cur")
      return 0
      ;;
  esac
  return 0
}
complete -o default -F _gdaldem gdaldem
_gdal_edit.py()
{
  local cur prev
  COMPREPLY=()
  _get_comp_words_by_ref cur prev
  case "$cur" in
    -*)
      key_list="--help-general -ro -a_srs -a_ullr -a_ulurll -tr -unsetgt -unsetrpc -a_nodata -unsetnodata -offset -scale -units -colorinterp_X -unsetstats -stats -approx_stats -setstats -gcp -unsetmd -oo -mo --version --build --license --formats --format --optfile --config --debug --pause --locale "
      mapfile -t COMPREPLY < <(compgen -W "$key_list" -- "$cur")
      return 0
      ;;
  esac
  tool=${COMP_WORDS[0]}
  case "$prev" in
    --format)
      key_list="$( $tool --formats | tail -n +2 | cut -f 3 -d ' ')"
      mapfile -t COMPREPLY < <(compgen -W "$key_list" -- "$cur")
      ;;
  esac
  return 0
}
complete -o default -F _gdal_edit.py gdal_edit.py
_gdalenhance()
{
  local cur prev
  COMPREPLY=()
  _get_comp_words_by_ref cur prev
  case "$cur" in
    -*)
      key_list="--help-general -of -co -ot -equalize -config --version --build --license --formats --format --optfile --config --debug --pause --locale "
      mapfile -t COMPREPLY < <(compgen -W "$key_list" -- "$cur")
      return 0
      ;;
  esac
  tool=${COMP_WORDS[0]}
  case "$prev" in
    -ot)
      key_list="Byte Int16 UInt16 UInt32 Int32 Float32 Float64 CInt16 CInt32 CFloat32 CFloat64"
      mapfile -t COMPREPLY < <(compgen -W "$key_list" -- "$cur")
      ;;
    -of)
      key_list="$( $tool --formats | tail -n +2 | cut -f 3 -d ' ')"
      mapfile -t COMPREPLY < <(compgen -W "$key_list" -- "$cur")
      ;;
    --format)
      key_list="$( $tool --formats | tail -n +2 | cut -f 3 -d ' ')"
      mapfile -t COMPREPLY < <(compgen -W "$key_list" -- "$cur")
      ;;
  esac
  return 0
}
complete -o default -F _gdalenhance gdalenhance
_gdal_fillnodata.py()
{
  local cur prev
  COMPREPLY=()
  _get_comp_words_by_ref cur prev
  case "$cur" in
    -*)
      key_list="-h -q -md -si -o -mask -b -of -co "
      mapfile -t COMPREPLY < <(compgen -W "$key_list" -- "$cur")
      return 0
      ;;
  esac
  tool=${COMP_WORDS[0]}
  case "$prev" in
    -of)
      key_list="$( $tool --formats | tail -n +2 | cut -f 3 -d ' ')"
      mapfile -t COMPREPLY < <(compgen -W "$key_list" -- "$cur")
      ;;
  esac
  return 0
}
complete -o default -F _gdal_fillnodata.py gdal_fillnodata.py
_gdal_grid()
{
  local cur prev
  COMPREPLY=()
  _get_comp_words_by_ref cur prev
  case "$cur" in
    -*)
      key_list="--help-general -ot -of -co -zfield -z_increase -z_multiply -a_srs -spat -clipsrc -clipsrcsql -clipsrclayer -clipsrcwhere -l -where -sql -txe -tye -tr -outsize -a -q --version --build --license --formats --format --optfile --config --debug --pause --locale "
      mapfile -t COMPREPLY < <(compgen -W "$key_list" -- "$cur")
      return 0
      ;;
  esac
  tool=${COMP_WORDS[0]}
  case "$prev" in
    -ot)
      key_list="Byte Int16 UInt16 UInt32 Int32 Float32 Float64 CInt16 CInt32 CFloat32 CFloat64"
      mapfile -t COMPREPLY < <(compgen -W "$key_list" -- "$cur")
      ;;
    -of)
      key_list="$( $tool --formats | tail -n +2 | cut -f 3 -d ' ')"
      mapfile -t COMPREPLY < <(compgen -W "$key_list" -- "$cur")
      ;;
    --format)
      key_list="$( $tool --formats | tail -n +2 | cut -f 3 -d ' ')"
      mapfile -t COMPREPLY < <(compgen -W "$key_list" -- "$cur")
      ;;
  esac
  return 0
}
complete -o default -F _gdal_grid gdal_grid
_gdalident.py()
{
  local cur prev
  COMPREPLY=()
  _get_comp_words_by_ref cur prev
  case "$cur" in
    -*)
      key_list=""
      mapfile -t COMPREPLY < <(compgen -W "$key_list" -- "$cur")
      return 0
      ;;
  esac
  return 0
}
complete -o default -F _gdalident.py gdalident.py
_gdalimport.py()
{
  local cur prev
  COMPREPLY=()
  _get_comp_words_by_ref cur prev
  case "$cur" in
    -*)
      key_list=""
      mapfile -t COMPREPLY < <(compgen -W "$key_list" -- "$cur")
      return 0
      ;;
  esac
  return 0
}
complete -o default -F _gdalimport.py gdalimport.py
_gdalinfo()
{
  local cur prev
  COMPREPLY=()
  _get_comp_words_by_ref cur prev
  case "$cur" in
    -*)
      key_list="--help-general -json -mm -stats -approx_stats -hist -nogcp -nomd -norat -noct -nofl -checksum -proj4 -listmdd -mdd -wkt_format -sd -oo -if --version --build --license --formats --format --optfile --config --debug --pause --locale "
      mapfile -t COMPREPLY < <(compgen -W "$key_list" -- "$cur")
      return 0
      ;;
  esac
  tool=${COMP_WORDS[0]}
  case "$prev" in
    --format)
      key_list="$( $tool --formats | tail -n +2 | cut -f 3 -d ' ')"
      mapfile -t COMPREPLY < <(compgen -W "$key_list" -- "$cur")
      ;;
  esac
  return 0
}
complete -o default -F _gdalinfo gdalinfo
_gdallocationinfo()
{
  local cur prev
  COMPREPLY=()
  _get_comp_words_by_ref cur prev
  case "$cur" in
    -*)
      key_list="--help-general -xml -lifonly -valonly -b -overview -l_srs -geoloc -wgs84 -oo --version --build --license --formats --format --optfile --config --debug --pause --locale "
      mapfile -t COMPREPLY < <(compgen -W "$key_list" -- "$cur")
      return 0
      ;;
  esac
  tool=${COMP_WORDS[0]}
  case "$prev" in
    --format)
      key_list="$( $tool --formats | tail -n +2 | cut -f 3 -d ' ')"
      mapfile -t COMPREPLY < <(compgen -W "$key_list" -- "$cur")
      ;;
  esac
  return 0
}
complete -o default -F _gdallocationinfo gdallocationinfo
_gdalmanage()
{
  local cur prev
  COMPREPLY=()
  _get_comp_words_by_ref cur prev
  case "$cur" in
    -*)
      key_list="-r -fr -u -f -f -f "
      mapfile -t COMPREPLY < <(compgen -W "$key_list" -- "$cur")
      return 0
      ;;
  esac
  return 0
}
complete -o default -F _gdalmanage gdalmanage
_gdal_merge.py()
{
  local cur prev
  COMPREPLY=()
  _get_comp_words_by_ref cur prev
  case "$cur" in
    -*)
      key_list="-o -of -co -ps -tap -separate -q -v -pct -ul_lr -init -n -a_nodata -ot -createonly --help-general --version --build --license --formats --format --optfile --config --debug --pause --locale "
      mapfile -t COMPREPLY < <(compgen -W "$key_list" -- "$cur")
      return 0
      ;;
  esac
  tool=${COMP_WORDS[0]}
  case "$prev" in
    -ot)
      key_list="Byte Int16 UInt16 UInt32 Int32 Float32 Float64 CInt16 CInt32 CFloat32 CFloat64"
      mapfile -t COMPREPLY < <(compgen -W "$key_list" -- "$cur")
      ;;
    -of)
      key_list="$( $tool --formats | tail -n +2 | cut -f 3 -d ' ')"
      mapfile -t COMPREPLY < <(compgen -W "$key_list" -- "$cur")
      ;;
    --format)
      key_list="$( $tool --formats | tail -n +2 | cut -f 3 -d ' ')"
      mapfile -t COMPREPLY < <(compgen -W "$key_list" -- "$cur")
      ;;
  esac
  return 0
}
complete -o default -F _gdal_merge.py gdal_merge.py
_gdalmove.py()
{
  local cur prev
  COMPREPLY=()
  _get_comp_words_by_ref cur prev
  case "$cur" in
    -*)
      key_list="-s_srs -t_srs -et "
      mapfile -t COMPREPLY < <(compgen -W "$key_list" -- "$cur")
      return 0
      ;;
  esac
  return 0
}
complete -o default -F _gdalmove.py gdalmove.py
_gdal_polygonize.py()
{
  local cur prev
  COMPREPLY=()
  _get_comp_words_by_ref cur prev
  case "$cur" in
    -*)
      key_list="-h -q -8 -o -mask -nomask -b -of "
      mapfile -t COMPREPLY < <(compgen -W "$key_list" -- "$cur")
      return 0
      ;;
  esac
  tool=${COMP_WORDS[0]}
  case "$prev" in
    -of)
      key_list="$( $tool --formats | tail -n +2 | cut -f 3 -d ' ')"
      mapfile -t COMPREPLY < <(compgen -W "$key_list" -- "$cur")
      ;;
  esac
  return 0
}
complete -o default -F _gdal_polygonize.py gdal_polygonize.py
_gdal_proximity.py()
{
  local cur prev
  COMPREPLY=()
  _get_comp_words_by_ref cur prev
  case "$cur" in
    -*)
      key_list="-srcband -dstband -of -co -ot -values -distunits -maxdist -nodata -use_input_nodata -fixed-buf-val -q "
      mapfile -t COMPREPLY < <(compgen -W "$key_list" -- "$cur")
      return 0
      ;;
  esac
  tool=${COMP_WORDS[0]}
  case "$prev" in
    -ot)
      key_list="Byte Int16 UInt16 UInt32 Int32 Float32 Float64 CInt16 CInt32 CFloat32 CFloat64"
      mapfile -t COMPREPLY < <(compgen -W "$key_list" -- "$cur")
      ;;
    -of)
      key_list="$( $tool --formats | tail -n +2 | cut -f 3 -d ' ')"
      mapfile -t COMPREPLY < <(compgen -W "$key_list" -- "$cur")
      ;;
  esac
  return 0
}
complete -o default -F _gdal_proximity.py gdal_proximity.py
_gdal_rasterize()
{
  local cur prev
  COMPREPLY=()
  _get_comp_words_by_ref cur prev
  case "$cur" in
    -*)
      key_list="-b -i -at -burn -a -3d -add -l -where -sql -dialect -of -a_srs -to -co -a_nodata -init -te -tr -tap -ts -ot -optim -q "
      mapfile -t COMPREPLY < <(compgen -W "$key_list" -- "$cur")
      return 0
      ;;
  esac
  tool=${COMP_WORDS[0]}
  case "$prev" in
    -ot)
      key_list="Byte Int16 UInt16 UInt32 Int32 Float32 Float64 CInt16 CInt32 CFloat32 CFloat64"
      mapfile -t COMPREPLY < <(compgen -W "$key_list" -- "$cur")
      ;;
    -of)
      key_list="$( $tool --formats | tail -n +2 | cut -f 3 -d ' ')"
      mapfile -t COMPREPLY < <(compgen -W "$key_list" -- "$cur")
      ;;
  esac
  return 0
}
complete -o default -F _gdal_rasterize gdal_rasterize
_gdal_retile.py()
{
  local cur prev
  COMPREPLY=()
  _get_comp_words_by_ref cur prev
  case "$cur" in
    -*)
      key_list="-v -q -co -of -ps -overlap -ot -tileIndex -tileIndexField -csv -csvDelim -s_srs -pyramidOnly -levels -r -useDirForEachRow -resume -targetDir "
      mapfile -t COMPREPLY < <(compgen -W "$key_list" -- "$cur")
      return 0
      ;;
  esac
  tool=${COMP_WORDS[0]}
  case "$prev" in
    -ot)
      key_list="Byte Int16 UInt16 UInt32 Int32 Float32 Float64 CInt16 CInt32 CFloat32 CFloat64"
      mapfile -t COMPREPLY < <(compgen -W "$key_list" -- "$cur")
      ;;
    -of)
      key_list="$( $tool --formats | tail -n +2 | cut -f 3 -d ' ')"
      mapfile -t COMPREPLY < <(compgen -W "$key_list" -- "$cur")
      ;;
  esac
  return 0
}
complete -o default -F _gdal_retile.py gdal_retile.py
_gdal_sieve.py()
{
  local cur prev
  COMPREPLY=()
  _get_comp_words_by_ref cur prev
  case "$cur" in
    -*)
      key_list=""
      mapfile -t COMPREPLY < <(compgen -W "$key_list" -- "$cur")
      return 0
      ;;
  esac
  return 0
}
complete -o default -F _gdal_sieve.py gdal_sieve.py
_gdalsrsinfo()
{
  local cur prev
  COMPREPLY=()
  _get_comp_words_by_ref cur prev
  case "$cur" in
    -*)
      key_list=""
      mapfile -t COMPREPLY < <(compgen -W "$key_list" -- "$cur")
      return 0
      ;;
  esac
  return 0
}
complete -o default -F _gdalsrsinfo gdalsrsinfo
_gdaltindex()
{
  local cur prev
  COMPREPLY=()
  _get_comp_words_by_ref cur prev
  case "$cur" in
    -*)
      key_list="-f -tileindex -write_absolute_path -skip_different_projection -t_srs -src_srs_name -src_srs_format -lyr_name "
      mapfile -t COMPREPLY < <(compgen -W "$key_list" -- "$cur")
      return 0
      ;;
  esac
  return 0
}
complete -o default -F _gdaltindex gdaltindex
_gdaltransform()
{
  local cur prev
  COMPREPLY=()
  _get_comp_words_by_ref cur prev
  case "$cur" in
    -*)
      key_list="--help-general -i -s_srs -t_srs -to -ct -order -tps -rpc -geoloc -gcp -output_xy --version --build --license --formats --format --optfile --config --debug --pause --locale "
      mapfile -t COMPREPLY < <(compgen -W "$key_list" -- "$cur")
      return 0
      ;;
  esac
  tool=${COMP_WORDS[0]}
  case "$prev" in
    --format)
      key_list="$( $tool --formats | tail -n +2 | cut -f 3 -d ' ')"
      mapfile -t COMPREPLY < <(compgen -W "$key_list" -- "$cur")
      ;;
  esac
  return 0
}
complete -o default -F _gdaltransform gdaltransform
_gdal_translate()
{
  local cur prev
  COMPREPLY=()
  _get_comp_words_by_ref cur prev
  case "$cur" in
    -*)
      key_list="--help-general --long-usage -ot -strict -if -of -b -mask -expand -outsize -tr -ovr -r -unscale -scale -exponent -srcwin -epo -eco -projwin -projwin_srs -a_srs -a_coord_epoch -a_ullr -a_nodata -a_scale -a_offset -nogcp -gcp -colorinterp{_bn} -colorinterp -mo -q -sds -co -stats -norat -noxmp -oo --version --build --license --formats --format --optfile --config --debug --pause --locale "
      mapfile -t COMPREPLY < <(compgen -W "$key_list" -- "$cur")
      return 0
      ;;
  esac
  tool=${COMP_WORDS[0]}
  case "$prev" in
    -ot)
      key_list="Byte Int16 UInt16 UInt32 Int32 Float32 Float64 CInt16 CInt32 CFloat32 CFloat64"
      mapfile -t COMPREPLY < <(compgen -W "$key_list" -- "$cur")
      ;;
    -of)
      key_list="$( $tool --formats | tail -n +2 | cut -f 3 -d ' ')"
      mapfile -t COMPREPLY < <(compgen -W "$key_list" -- "$cur")
      ;;
    --format)
      key_list="$( $tool --formats | tail -n +2 | cut -f 3 -d ' ')"
      mapfile -t COMPREPLY < <(compgen -W "$key_list" -- "$cur")
      ;;
  esac
  return 0
}
complete -o default -F _gdal_translate gdal_translate
_gdalwarp()
{
  local cur prev
  COMPREPLY=()
  _get_comp_words_by_ref cur prev
  case "$cur" in
    -*)
      key_list="--help-general --formats -s_srs -t_srs -to -vshift -novshift -s_coord_epoch -t_coord_epoch -order -tps -rpc -geoloc -et -refine_gcps -te -tr -tap -ts -ovr -wo -ot -wt -srcnodata -dstnodata -dstalpha -r -wm -multi -q -cutline -cl -cwhere -csql -cblend -crop_to_cutline -if -of -co -overwrite -nomd -cvmd -setci -oo -doo --version --build --license --format --optfile --config --debug --pause --locale "
      mapfile -t COMPREPLY < <(compgen -W "$key_list" -- "$cur")
      return 0
      ;;
  esac
  tool=${COMP_WORDS[0]}
  case "$prev" in
    -ot)
      key_list="Byte Int16 UInt16 UInt32 Int32 Float32 Float64 CInt16 CInt32 CFloat32 CFloat64"
      mapfile -t COMPREPLY < <(compgen -W "$key_list" -- "$cur")
      ;;
    -of)
      key_list="$( $tool --formats | tail -n +2 | cut -f 3 -d ' ')"
      mapfile -t COMPREPLY < <(compgen -W "$key_list" -- "$cur")
      ;;
    --format)
      key_list="$( $tool --formats | tail -n +2 | cut -f 3 -d ' ')"
      mapfile -t COMPREPLY < <(compgen -W "$key_list" -- "$cur")
      ;;
  esac
  return 0
}
complete -o default -F _gdalwarp gdalwarp
_gdal_viewshed()
{
  local cur prev
  COMPREPLY=()
  _get_comp_words_by_ref cur prev
  case "$cur" in
    -*)
      key_list="-b -a_nodata -f -oz -tz -md -ox -oy -vv -iv -ov -cc -co -q -om "
      mapfile -t COMPREPLY < <(compgen -W "$key_list" -- "$cur")
      return 0
      ;;
  esac
  return 0
}
complete -o default -F _gdal_viewshed gdal_viewshed
_gdal_create()
{
  local cur prev
  COMPREPLY=()
  _get_comp_words_by_ref cur prev
  case "$cur" in
    -*)
      key_list="--help-general -of -outsize -bands -burn -ot -strict -a_srs -a_ullr -a_nodata -mo -q -co -if --version --build --license --formats --format --optfile --config --debug --pause --locale "
      mapfile -t COMPREPLY < <(compgen -W "$key_list" -- "$cur")
      return 0
      ;;
  esac
  tool=${COMP_WORDS[0]}
  case "$prev" in
    -ot)
      key_list="Byte Int16 UInt16 UInt32 Int32 Float32 Float64 CInt16 CInt32 CFloat32 CFloat64"
      mapfile -t COMPREPLY < <(compgen -W "$key_list" -- "$cur")
      ;;
    -of)
      key_list="$( $tool --formats | tail -n +2 | cut -f 3 -d ' ')"
      mapfile -t COMPREPLY < <(compgen -W "$key_list" -- "$cur")
      ;;
    --format)
      key_list="$( $tool --formats | tail -n +2 | cut -f 3 -d ' ')"
      mapfile -t COMPREPLY < <(compgen -W "$key_list" -- "$cur")
      ;;
  esac
  return 0
}
complete -o default -F _gdal_create gdal_create
_ogr2ogr()
{
  local cur prev
  COMPREPLY=()
  _get_comp_words_by_ref cur prev
  case "$cur" in
    -*)
      key_list="--help-general -skipfailures -append -upsert -update -select -where -progress -sql -dialect -preserve_fid -fid -limit -spat -spat_srs -geomfield -a_srs -t_srs -s_srs -ct -f -overwrite -dsco -lco -nln -nlt -dim --version --build --license --formats --format --optfile --config --debug --pause --locale "
      mapfile -t COMPREPLY < <(compgen -W "$key_list" -- "$cur")
      return 0
      ;;
  esac
  tool=${COMP_WORDS[0]/ogrtindex/ogr2ogr}
  case "$prev" in
    -f)
      key_list="$( $tool --formats | tail -n +2 | grep -o -E '"[^"]+"' | sed 's/\ /__/')"
      for iter in $key_list; do
        if [[ $iter =~ ^$cur ]]; then
          COMPREPLY+=( "${iter//__/ }" )
        fi
      done
      ;;
  esac
  return 0
}
complete -o default -F _ogr2ogr ogr2ogr
_ogrinfo()
{
  local cur prev
  COMPREPLY=()
  _get_comp_words_by_ref cur prev
  case "$cur" in
    -*)
      key_list="--help-general -ro -q -where -spat -geomfield -fid -sql -dialect -al -rl -so -fields=YES -fields=NO -geom=YES -geom=NO -geom=SUMMARY -oo -nomd -listmdd -mdd -nocount -noextent -nogeomtype -wkt_format -fielddomain --version --build --license --formats --format --optfile --config --debug --pause --locale "
      mapfile -t COMPREPLY < <(compgen -W "$key_list" -- "$cur")
      return 0
      ;;
  esac
  return 0
}
complete -o default -F _ogrinfo ogrinfo
_ogrlineref()
{
  local cur prev
  COMPREPLY=()
  _get_comp_words_by_ref cur prev
  case "$cur" in
    -*)
      key_list="--help-general -progress -quiet -f -dsco -lco -create -l -ln -lf -p -pn -pm -pf -r -rn -o -on -of -s -get_pos -x -y -get_coord -m -get_subline -mb -me --version --build --license --formats --format --optfile --config --debug --pause --locale "
      mapfile -t COMPREPLY < <(compgen -W "$key_list" -- "$cur")
      return 0
      ;;
  esac
  tool=${COMP_WORDS[0]/ogrtindex/ogr2ogr}
  case "$prev" in
    -f)
      key_list="$( $tool --formats | tail -n +2 | grep -o -E '"[^"]+"' | sed 's/\ /__/')"
      for iter in $key_list; do
        if [[ $iter =~ ^$cur ]]; then
          COMPREPLY+=( "${iter//__/ }" )
        fi
      done
      ;;
    -of)
      key_list="$( $tool --formats | tail -n +2 | grep -o -E '"[^"]+"' | sed 's/\ /__/')"
      for iter in $key_list; do
        if [[ $iter =~ ^$cur ]]; then
          COMPREPLY+=( "${iter//__/ }" )
        fi
      done
      ;;
  esac
  return 0
}
complete -o default -F _ogrlineref ogrlineref
_ogrtindex()
{
  local cur prev
  COMPREPLY=()
  _get_comp_words_by_ref cur prev
  case "$cur" in
    -*)
      key_list="-lnum -lname -f -write_absolute_path -skip_different_projection -t_srs -src_srs_name -src_srs_format -accept_different_schemas "
      mapfile -t COMPREPLY < <(compgen -W "$key_list" -- "$cur")
      return 0
      ;;
  esac
  tool=${COMP_WORDS[0]/ogrtindex/ogr2ogr}
  case "$prev" in
    -f)
      key_list="$( $tool --formats | tail -n +2 | grep -o -E '"[^"]+"' | sed 's/\ /__/')"
      for iter in $key_list; do
        if [[ $iter =~ ^$cur ]]; then
          COMPREPLY+=( "${iter//__/ }" )
        fi
      done
      ;;
  esac
  return 0
}
complete -o default -F _ogrtindex ogrtindex
_ogrmerge.py()
{
  local cur prev
  COMPREPLY=()
  _get_comp_words_by_ref cur prev
  case "$cur" in
    -*)
      key_list="-o -f -single -nln -update -overwrite_ds -append -overwrite_layer -src_geom_type -dsco -lco -s_srs -t_srs -a_srs -progress -skipfailures --help-general --version --build --license --formats --format --optfile --config --debug --pause --locale "
      mapfile -t COMPREPLY < <(compgen -W "$key_list" -- "$cur")
      return 0
      ;;
  esac
  tool=${COMP_WORDS[0]/ogrtindex/ogr2ogr}
  case "$prev" in
    -f)
      key_list="$( $tool --formats | tail -n +2 | grep -o -E '"[^"]+"' | sed 's/\ /__/')"
      for iter in $key_list; do
        if [[ $iter =~ ^$cur ]]; then
          COMPREPLY+=( "${iter//__/ }" )
        fi
      done
      ;;
  esac
  return 0
}
complete -o default -F _ogrmerge.py ogrmerge.py
_ogr_layer_algebra.py()
{
  local cur prev
  COMPREPLY=()
  _get_comp_words_by_ref cur prev
  case "$cur" in
    -*)
      key_list="-input_ds -input_lyr -method_ds -method_lyr -output_ds -output_lyr -overwrite -opt -f -dsco -lco -input_fields -method_fields -nlt -a_srs "
      mapfile -t COMPREPLY < <(compgen -W "$key_list" -- "$cur")
      return 0
      ;;
  esac
  tool=${COMP_WORDS[0]/ogrtindex/ogr2ogr}
  case "$prev" in
    -f)
      key_list="$( $tool --formats | tail -n +2 | grep -o -E '"[^"]+"' | sed 's/\ /__/')"
      for iter in $key_list; do
        if [[ $iter =~ ^$cur ]]; then
          COMPREPLY+=( "${iter//__/ }" )
        fi
      done
      ;;
  esac
  return 0
}
complete -o default -F _ogr_layer_algebra.py ogr_layer_algebra.py
