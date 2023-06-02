package !mod.java_pkg.Items;

import net.fabricmc.api.ModInitializer;
import net.fabricmc.fabric.api.item.v1.FabricItemSettings;
import net.minecraft.item.Item;
import net.minecraft.item.FoodComponents;
import net.minecraft.registry.Registries;
import net.minecraft.registry.Registry;
import net.minecraft.util.Identifier;

public class !item.id implements ModInitializer {
    public static final Item THIS_ITEM = Registry.register(Registries.ITEM, new Identifier("!mod.id", "!item.id"), new Item(new FabricItemSettings()!item.edible));

    @Override
    public void onInitialize() {
    }
}