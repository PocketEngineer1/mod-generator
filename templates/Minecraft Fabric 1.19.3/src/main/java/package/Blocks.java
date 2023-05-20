package !mod.java_pkg.Blocks;

import net.fabricmc.api.ModInitializer;
import net.fabricmc.fabric.api.item.v1.FabricItemSettings;
import net.fabricmc.fabric.api.object.builder.v1.block.FabricBlockSettings;
import net.minecraft.block.Block;
import net.minecraft.block.Material;
import net.minecraft.item.BlockItem;
import net.minecraft.registry.Registries;
import net.minecraft.registry.Registry;
import net.minecraft.util.Identifier;

public class !block.id implements ModInitializer {
    public static final Block THIS_BLOCK = new Block(FabricBlockSettings.of(Material.METAL).strength(1.0f));
	
    @Override
    public void onInitialize() {
        Registry.register(Registries.BLOCK, new Identifier("!mod.id", "!block.id"), THIS_BLOCK);
        Registry.register(Registries.ITEM, new Identifier("!mod.id", "!block.id"), new BlockItem(THIS_BLOCK, new FabricItemSettings()));
    }
}