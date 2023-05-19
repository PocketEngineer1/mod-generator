package !mod.java_pkg.Blocks;

import net.fabricmc.api.ModInitializer;
import net.fabricmc.fabric.api.item.v1.FabricItemSettings;
import net.minecraft.item.Item;
import net.minecraft.registry.Registries;
import net.minecraft.registry.Registry;
import net.minecraft.util.Identifier;

public class !block.id implements ModInitializer {
    public static final Item THIS_BLOCK = Registry.register(Registries.ITEM, new Identifier("!mod.id", "!item.id"), new Item(new FabricItemSettings()));

    @Override
    public void onInitialize() {
    }
}