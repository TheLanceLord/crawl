/**
 * @file
 * @brief Functions used to print information about gods.
 **/

#ifndef DESCRIBE_GOD_H
#define DESCRIBE_GOD_H

enum god_desc_type
{
    GDESC_OVERVIEW,
    GDESC_DETAILED,
    GDESC_WRATH,
    NUM_GDESCS
};

string god_title(god_type which_god, species_type which_species, int piety);
void describe_god(god_type which_god, bool give_title,
                  god_desc_type gdesc = GDESC_OVERVIEW);

#endif
